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


class DecryptedMessageMediaDocument(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``6ABD9782``

    Parameters:
        thumb: ``bytes``
        thumb_w: ``int`` ``32-bit``
        thumb_h: ``int`` ``32-bit``
        mime_type: ``str``
        size: ``int`` ``64-bit``
        key: ``bytes``
        iv: ``bytes``
        attributes: List of :obj:`DocumentAttribute <pyrogram_secret_chat.raw.base.DocumentAttribute>`
        caption: ``str``
    """

    __slots__: List[str] = ["thumb", "thumb_w", "thumb_h", "mime_type", "size", "key", "iv", "attributes", "caption"]

    ID = 0x6abd9782
    QUALNAME = "e2e.DecryptedMessageMediaDocument"

    def __init__(self, *, thumb: bytes, thumb_w: int, thumb_h: int, mime_type: str, size: int, key: bytes, iv: bytes, attributes: List["raw.base.DocumentAttribute"], caption: str) -> None:
        self.thumb = thumb  # bytes
        self.thumb_w = thumb_w  # int
        self.thumb_h = thumb_h  # int
        self.mime_type = mime_type  # string
        self.size = size  # long
        self.key = key  # bytes
        self.iv = iv  # bytes
        self.attributes = attributes  # Vector<DocumentAttribute>
        self.caption = caption  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessageMediaDocument":
        # No flags
        
        thumb = Bytes.read(b)
        
        thumb_w = Int.read(b)
        
        thumb_h = Int.read(b)
        
        mime_type = String.read(b)
        
        size = Long.read(b)
        
        key = Bytes.read(b)
        
        iv = Bytes.read(b)
        
        attributes = TLObject.read(b)
        
        caption = String.read(b)
        
        return DecryptedMessageMediaDocument(thumb=thumb, thumb_w=thumb_w, thumb_h=thumb_h, mime_type=mime_type, size=size, key=key, iv=iv, attributes=attributes, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.thumb))
        
        b.write(Int(self.thumb_w))
        
        b.write(Int(self.thumb_h))
        
        b.write(String(self.mime_type))
        
        b.write(Long(self.size))
        
        b.write(Bytes(self.key))
        
        b.write(Bytes(self.iv))
        
        b.write(Vector(self.attributes))
        
        b.write(String(self.caption))
        
        return b.getvalue()
