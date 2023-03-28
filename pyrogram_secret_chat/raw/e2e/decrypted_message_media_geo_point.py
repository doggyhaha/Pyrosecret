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


class DecryptedMessageMediaGeoPoint(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``35480A59``

    Parameters:
        lat: ``float`` ``64-bit``
        long: ``float`` ``64-bit``
    """

    __slots__: List[str] = ["lat", "long"]

    ID = 0x35480a59
    QUALNAME = "e2e.DecryptedMessageMediaGeoPoint"

    def __init__(self, *, lat: float, long: float) -> None:
        self.lat = lat  # double
        self.long = long  # double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessageMediaGeoPoint":
        # No flags
        
        lat = Double.read(b)
        
        long = Double.read(b)
        
        return DecryptedMessageMediaGeoPoint(lat=lat, long=long)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Double(self.lat))
        
        b.write(Double(self.long))
        
        return b.getvalue()
