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


class DecryptedMessageMediaVenue(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``8A0DF56F``

    Parameters:
        lat: ``float`` ``64-bit``
        long: ``float`` ``64-bit``
        title: ``str``
        address: ``str``
        provider: ``str``
        venue_id: ``str``
    """

    __slots__: List[str] = ["lat", "long", "title", "address", "provider", "venue_id"]

    ID = 0x8a0df56f
    QUALNAME = "e2e.DecryptedMessageMediaVenue"

    def __init__(self, *, lat: float, long: float, title: str, address: str, provider: str, venue_id: str) -> None:
        self.lat = lat  # double
        self.long = long  # double
        self.title = title  # string
        self.address = address  # string
        self.provider = provider  # string
        self.venue_id = venue_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessageMediaVenue":
        # No flags
        
        lat = Double.read(b)
        
        long = Double.read(b)
        
        title = String.read(b)
        
        address = String.read(b)
        
        provider = String.read(b)
        
        venue_id = String.read(b)
        
        return DecryptedMessageMediaVenue(lat=lat, long=long, title=title, address=address, provider=provider, venue_id=venue_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Double(self.lat))
        
        b.write(Double(self.long))
        
        b.write(String(self.title))
        
        b.write(String(self.address))
        
        b.write(String(self.provider))
        
        b.write(String(self.venue_id))
        
        return b.getvalue()
