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


class DecryptedMessageMediaExternalDocument(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``FA95B0DD``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        date: ``int`` ``32-bit``
        mime_type: ``str``
        size: ``int`` ``32-bit``
        thumb: :obj:`PhotoSize <pyrogram_secret_chat.raw.base.PhotoSize>`
        dc_id: ``int`` ``32-bit``
        attributes: List of :obj:`DocumentAttribute <pyrogram_secret_chat.raw.base.DocumentAttribute>`
    """

    __slots__: List[str] = ["id", "access_hash", "date", "mime_type", "size", "thumb", "dc_id", "attributes"]

    ID = 0xfa95b0dd
    QUALNAME = "e2e.DecryptedMessageMediaExternalDocument"

    def __init__(self, *, id: int, access_hash: int, date: int, mime_type: str, size: int, thumb: "raw.base.PhotoSize", dc_id: int, attributes: List["raw.base.DocumentAttribute"]) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.mime_type = mime_type  # string
        self.size = size  # int
        self.thumb = thumb  # PhotoSize
        self.dc_id = dc_id  # int
        self.attributes = attributes  # Vector<DocumentAttribute>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessageMediaExternalDocument":
        # No flags
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        mime_type = String.read(b)
        
        size = Int.read(b)
        
        thumb = TLObject.read(b)
        
        dc_id = Int.read(b)
        
        attributes = TLObject.read(b)
        
        return DecryptedMessageMediaExternalDocument(id=id, access_hash=access_hash, date=date, mime_type=mime_type, size=size, thumb=thumb, dc_id=dc_id, attributes=attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(String(self.mime_type))
        
        b.write(Int(self.size))
        
        b.write(self.thumb.write())
        
        b.write(Int(self.dc_id))
        
        b.write(Vector(self.attributes))
        
        return b.getvalue()
