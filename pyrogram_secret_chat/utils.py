#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
import functools
import inspect
import io
import logging
import math
import os
from hashlib import md5
from pathlib import PurePath
from typing import Union, BinaryIO, Callable, cast

import pyrogram
from pyrogram import StopTransmission
from pyrogram import raw
from pyrogram.session import Session
from pyrogram.crypto import aes
from pyrogram.raw.types import EncryptedFileEmpty

from .types import SecretMessage
from .raw.e2e import DecryptedMessageMediaPhoto, DecryptedMessageMediaPhoto8

log = logging.getLogger(__name__)

photos = (DecryptedMessageMediaPhoto, DecryptedMessageMediaPhoto8)

part_size = 512 * 1024


async def upload_encrypted_doc( #fuck it, save_file with encryption support
    self: "pyrogram.Client",
    path: Union[str, BinaryIO],
    file_id: int = None,
    file_part: int = 0,
    progress: Callable = None,
    progress_args: tuple = (),
    key: bytes = b'',
    iv: bytes = b''
):
    if path is None:
        return None

    async def worker(session):
        while True:
            data = await queue.get()

            if data is None:
                return

            try:
                await session.invoke(data)
            except Exception as e:
                log.error(e)

    if isinstance(path, (str, PurePath)):
        fp = open(path, "rb")
    elif isinstance(path, io.IOBase):
        fp = path
    else:
        raise ValueError("Invalid file. Expected a file path as string or a binary (not text) file pointer")

    file_name = getattr(fp, "name", "file.jpg")

    fp.seek(0, os.SEEK_END)
    file_size = fp.tell()
    fp.seek(0)

    if file_size == 0:
        raise ValueError("File size equals to 0 B")

    file_size_limit_mib = 4000 if self.me.is_premium else 2000

    if file_size > file_size_limit_mib * 1024 * 1024:
        raise ValueError(f"Can't upload files bigger than {file_size_limit_mib} MiB")

    file_total_parts = int(math.ceil(file_size / part_size))
    is_big = file_size > 10 * 1024 * 1024
    pool_size = 3 if is_big else 1
    workers_count = 4 if is_big else 1
    is_missing_part = file_id is not None
    file_id = file_id or self.rnd_id()
    md5_sum = md5() if not is_big and not is_missing_part else None
    pool = [
        Session(
            self, await self.storage.dc_id(), await self.storage.auth_key(),
            await self.storage.test_mode(), is_media=True
        ) for _ in range(pool_size)
    ]
    workers = [self.loop.create_task(worker(session)) for session in pool for _ in range(workers_count)]
    queue = asyncio.Queue(16)

    try:
        for session in pool:
            await session.start()

        fp.seek(part_size * file_part)

        while True:
            chunk = fp.read(part_size)
            if key != b'' and iv != b'':
                chunk = aes.ige256_encrypt(chunk, key, iv)

            if not chunk:
                if not is_big and not is_missing_part:
                    md5_sum = "".join([hex(i)[2:].zfill(2) for i in md5_sum.digest()])
                break

            if is_big:
                rpc = raw.functions.upload.SaveBigFilePart(
                    file_id=file_id,
                    file_part=file_part,
                    file_total_parts=file_total_parts,
                    bytes=chunk
                )
            else:
                rpc = raw.functions.upload.SaveFilePart(
                    file_id=file_id,
                    file_part=file_part,
                    bytes=chunk
                )

            await queue.put(rpc)

            if is_missing_part:
                return

            if not is_big and not is_missing_part:
                md5_sum.update(chunk)

            file_part += 1

            if progress:
                func = functools.partial(
                    progress,
                    min(file_part * part_size, file_size),
                    file_size,
                    *progress_args
                )

                if inspect.iscoroutinefunction(progress):
                    await func()
                else:
                    await self.loop.run_in_executor(self.executor, func)
    except StopTransmission:
        raise
    except Exception as e:
        log.error(e, exc_info=True)
    else:
        if is_big:
            return raw.types.InputFileBig(
                id=file_id,
                parts=file_total_parts,
                name=file_name,

            )
        else:
            return raw.types.InputFile(
                id=file_id,
                parts=file_total_parts,
                name=file_name,
                md5_checksum=md5_sum
            )
    finally:
        for _ in workers:
            await queue.put(None)

        await asyncio.gather(*workers)

        for session in pool:
            await session.stop()

        if isinstance(path, (str, PurePath)):
            fp.close()

def save_photo(msg: SecretMessage, out=Union[str, io.BytesIO]) -> Union[str, io.BytesIO]:
    if isinstance(msg.file, EncryptedFileEmpty):
        raise ValueError("Message doesn't contain any media")
    if not isinstance(msg.raw.media, photos):
        raise ValueError("Message media doesn't seem to be a photo")
    else:
        data = msg.raw.media.thumb
        key = msg.raw.media.key
        iv = msg.raw.media.iv
        fp = out if isinstance(out, io.BytesIO) else open(out, "wb")
        fp.write(data)

        while True:
            ochunk = fp.read(part_size)
            if not ochunk:
                break
            chunk = aes.ige256_decrypt(ochunk, key, iv)
            fp.seek(fp.tell()-len(ochunk))
            fp.write(chunk)
        
        if isinstance(out, str):
            fp.close()
            return out
        else:
            return fp