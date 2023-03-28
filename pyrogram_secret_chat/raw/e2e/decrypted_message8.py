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


class DecryptedMessage8(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``1F814F1F``

    Parameters:
        random_id: ``int`` ``64-bit``
        random_bytes: ``bytes``
        message: ``str``
        media: :obj:`DecryptedMessageMedia <pyrogram_secret_chat.raw.base.DecryptedMessageMedia>`
    """

    __slots__: List[str] = ["random_id", "random_bytes", "message", "media"]

    ID = 0x1f814f1f
    QUALNAME = "e2e.DecryptedMessage8"

    def __init__(self, *, random_id: int, random_bytes: bytes, message: str, media: "raw.base.DecryptedMessageMedia") -> None:
        self.random_id = random_id  # long
        self.random_bytes = random_bytes  # bytes
        self.message = message  # string
        self.media = media  # DecryptedMessageMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessage8":
        # No flags
        
        random_id = Long.read(b)
        
        random_bytes = Bytes.read(b)
        
        message = String.read(b)
        
        media = TLObject.read(b)
        
        return DecryptedMessage8(random_id=random_id, random_bytes=random_bytes, message=message, media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.random_id))
        
        b.write(Bytes(self.random_bytes))
        
        b.write(String(self.message))
        
        b.write(self.media.write())
        
        return b.getvalue()
