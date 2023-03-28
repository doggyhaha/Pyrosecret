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


class DocumentAttributeAudio45(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``DED218E0``

    Parameters:
        duration: ``int`` ``32-bit``
        title: ``str``
        performer: ``str``
    """

    __slots__: List[str] = ["duration", "title", "performer"]

    ID = 0xded218e0
    QUALNAME = "e2e.DocumentAttributeAudio45"

    def __init__(self, *, duration: int, title: str, performer: str) -> None:
        self.duration = duration  # int
        self.title = title  # string
        self.performer = performer  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeAudio45":
        # No flags
        
        duration = Int.read(b)
        
        title = String.read(b)
        
        performer = String.read(b)
        
        return DocumentAttributeAudio45(duration=duration, title=title, performer=performer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.duration))
        
        b.write(String(self.title))
        
        b.write(String(self.performer))
        
        return b.getvalue()
