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


class DecryptedMessageMediaVideo8(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``4CEE6EF3``

    Parameters:
        thumb: ``bytes``
        thumb_w: ``int`` ``32-bit``
        thumb_h: ``int`` ``32-bit``
        duration: ``int`` ``32-bit``
        w: ``int`` ``32-bit``
        h: ``int`` ``32-bit``
        size: ``int`` ``32-bit``
        key: ``bytes``
        iv: ``bytes``
    """

    __slots__: List[str] = ["thumb", "thumb_w", "thumb_h", "duration", "w", "h", "size", "key", "iv"]

    ID = 0x4cee6ef3
    QUALNAME = "e2e.DecryptedMessageMediaVideo8"

    def __init__(self, *, thumb: bytes, thumb_w: int, thumb_h: int, duration: int, w: int, h: int, size: int, key: bytes, iv: bytes) -> None:
        self.thumb = thumb  # bytes
        self.thumb_w = thumb_w  # int
        self.thumb_h = thumb_h  # int
        self.duration = duration  # int
        self.w = w  # int
        self.h = h  # int
        self.size = size  # int
        self.key = key  # bytes
        self.iv = iv  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessageMediaVideo8":
        # No flags
        
        thumb = Bytes.read(b)
        
        thumb_w = Int.read(b)
        
        thumb_h = Int.read(b)
        
        duration = Int.read(b)
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        size = Int.read(b)
        
        key = Bytes.read(b)
        
        iv = Bytes.read(b)
        
        return DecryptedMessageMediaVideo8(thumb=thumb, thumb_w=thumb_w, thumb_h=thumb_h, duration=duration, w=w, h=h, size=size, key=key, iv=iv)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.thumb))
        
        b.write(Int(self.thumb_w))
        
        b.write(Int(self.thumb_h))
        
        b.write(Int(self.duration))
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        b.write(Int(self.size))
        
        b.write(Bytes(self.key))
        
        b.write(Bytes(self.iv))
        
        return b.getvalue()
