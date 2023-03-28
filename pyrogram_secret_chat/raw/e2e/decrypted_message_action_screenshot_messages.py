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


class DecryptedMessageActionScreenshotMessages(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``8AC1F475``

    Parameters:
        random_ids: List of ``int`` ``64-bit``
    """

    __slots__: List[str] = ["random_ids"]

    ID = 0x8ac1f475
    QUALNAME = "e2e.DecryptedMessageActionScreenshotMessages"

    def __init__(self, *, random_ids: List[int]) -> None:
        self.random_ids = random_ids  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessageActionScreenshotMessages":
        # No flags
        
        random_ids = TLObject.read(b, Long)
        
        return DecryptedMessageActionScreenshotMessages(random_ids=random_ids)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.random_ids, Long))
        
        return b.getvalue()
