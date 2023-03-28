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


class DecryptedMessageMediaAudio8(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``6080758F``

    Parameters:
        duration: ``int`` ``32-bit``
        size: ``int`` ``32-bit``
        key: ``bytes``
        iv: ``bytes``
    """

    __slots__: List[str] = ["duration", "size", "key", "iv"]

    ID = 0x6080758f
    QUALNAME = "e2e.DecryptedMessageMediaAudio8"

    def __init__(self, *, duration: int, size: int, key: bytes, iv: bytes) -> None:
        self.duration = duration  # int
        self.size = size  # int
        self.key = key  # bytes
        self.iv = iv  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessageMediaAudio8":
        # No flags
        
        duration = Int.read(b)
        
        size = Int.read(b)
        
        key = Bytes.read(b)
        
        iv = Bytes.read(b)
        
        return DecryptedMessageMediaAudio8(duration=duration, size=size, key=key, iv=iv)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.duration))
        
        b.write(Int(self.size))
        
        b.write(Bytes(self.key))
        
        b.write(Bytes(self.iv))
        
        return b.getvalue()
