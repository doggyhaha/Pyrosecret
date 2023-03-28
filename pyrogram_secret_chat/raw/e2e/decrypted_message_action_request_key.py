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


class DecryptedMessageActionRequestKey(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``F3C9611B``

    Parameters:
        exchange_id: ``int`` ``64-bit``
        g_a: ``bytes``
    """

    __slots__: List[str] = ["exchange_id", "g_a"]

    ID = 0xf3c9611b
    QUALNAME = "e2e.DecryptedMessageActionRequestKey"

    def __init__(self, *, exchange_id: int, g_a: bytes) -> None:
        self.exchange_id = exchange_id  # long
        self.g_a = g_a  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessageActionRequestKey":
        # No flags
        
        exchange_id = Long.read(b)
        
        g_a = Bytes.read(b)
        
        return DecryptedMessageActionRequestKey(exchange_id=exchange_id, g_a=g_a)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.exchange_id))
        
        b.write(Bytes(self.g_a))
        
        return b.getvalue()
