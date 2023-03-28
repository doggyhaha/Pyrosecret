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


class DocumentAttributeVideo23(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``5910CCCB``

    Parameters:
        duration: ``int`` ``32-bit``
        w: ``int`` ``32-bit``
        h: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["duration", "w", "h"]

    ID = 0x5910cccb
    QUALNAME = "e2e.DocumentAttributeVideo23"

    def __init__(self, *, duration: int, w: int, h: int) -> None:
        self.duration = duration  # int
        self.w = w  # int
        self.h = h  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeVideo23":
        # No flags
        
        duration = Int.read(b)
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        return DocumentAttributeVideo23(duration=duration, w=w, h=h)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.duration))
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        return b.getvalue()
