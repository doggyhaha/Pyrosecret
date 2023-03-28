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


class DecryptedMessageActionResend(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``511110B0``

    Parameters:
        start_seq_no: ``int`` ``32-bit``
        end_seq_no: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["start_seq_no", "end_seq_no"]

    ID = 0x511110b0
    QUALNAME = "e2e.DecryptedMessageActionResend"

    def __init__(self, *, start_seq_no: int, end_seq_no: int) -> None:
        self.start_seq_no = start_seq_no  # int
        self.end_seq_no = end_seq_no  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessageActionResend":
        # No flags
        
        start_seq_no = Int.read(b)
        
        end_seq_no = Int.read(b)
        
        return DecryptedMessageActionResend(start_seq_no=start_seq_no, end_seq_no=end_seq_no)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.start_seq_no))
        
        b.write(Int(self.end_seq_no))
        
        return b.getvalue()
