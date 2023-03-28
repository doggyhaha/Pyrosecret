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

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class DecryptedMessage(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``91CC4674``

    Parameters:
        random_id: ``int`` ``64-bit``
        ttl: ``int`` ``32-bit``
        message: ``str``
        silent (optional): ``bool``
        media (optional): :obj:`DecryptedMessageMedia <pyrogram_secret_chat.raw.base.DecryptedMessageMedia>`
        entities (optional): List of :obj:`MessageEntity <pyrogram_secret_chat.raw.base.MessageEntity>`
        via_bot_name (optional): ``str``
        reply_to_random_id (optional): ``int`` ``64-bit``
        grouped_id (optional): ``int`` ``64-bit``
    """

    __slots__: List[str] = ["random_id", "ttl", "message", "silent", "media", "entities", "via_bot_name", "reply_to_random_id", "grouped_id"]

    ID = 0x91cc4674
    QUALNAME = "e2e.DecryptedMessage"

    def __init__(self, *, random_id: int, ttl: int, message: str, silent: Optional[bool] = None, media: "raw.base.DecryptedMessageMedia" = None, entities: Optional[List["raw.base.MessageEntity"]] = None, via_bot_name: Optional[str] = None, reply_to_random_id: Optional[int] = None, grouped_id: Optional[int] = None) -> None:
        self.random_id = random_id  # long
        self.ttl = ttl  # int
        self.message = message  # string
        self.silent = silent  # flags.5?true
        self.media = media  # flags.9?DecryptedMessageMedia
        self.entities = entities  # flags.7?Vector<MessageEntity>
        self.via_bot_name = via_bot_name  # flags.11?string
        self.reply_to_random_id = reply_to_random_id  # flags.3?long
        self.grouped_id = grouped_id  # flags.17?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessage":
        
        flags = Int.read(b)
        
        silent = True if flags & (1 << 5) else False
        random_id = Long.read(b)
        
        ttl = Int.read(b)
        
        message = String.read(b)
        
        media = TLObject.read(b) if flags & (1 << 9) else None
        
        entities = TLObject.read(b) if flags & (1 << 7) else []
        
        via_bot_name = String.read(b) if flags & (1 << 11) else None
        reply_to_random_id = Long.read(b) if flags & (1 << 3) else None
        grouped_id = Long.read(b) if flags & (1 << 17) else None
        return DecryptedMessage(random_id=random_id, ttl=ttl, message=message, silent=silent, media=media, entities=entities, via_bot_name=via_bot_name, reply_to_random_id=reply_to_random_id, grouped_id=grouped_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 9) if self.media is not None else 0
        flags |= (1 << 7) if self.entities else 0
        flags |= (1 << 11) if self.via_bot_name is not None else 0
        flags |= (1 << 3) if self.reply_to_random_id is not None else 0
        flags |= (1 << 17) if self.grouped_id is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.random_id))
        
        b.write(Int(self.ttl))
        
        b.write(String(self.message))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.entities:
            b.write(Vector(self.entities))
        
        if self.via_bot_name is not None:
            b.write(String(self.via_bot_name))
        
        if self.reply_to_random_id is not None:
            b.write(Long(self.reply_to_random_id))
        
        if self.grouped_id is not None:
            b.write(Long(self.grouped_id))
        
        return b.getvalue()
