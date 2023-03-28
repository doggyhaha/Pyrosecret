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


class DecryptedMessageActionAcceptKey(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``6FE1735B``

    Parameters:
        exchange_id: ``int`` ``64-bit``
        g_b: ``bytes``
        key_fingerprint: ``int`` ``64-bit``
    """

    __slots__: List[str] = ["exchange_id", "g_b", "key_fingerprint"]

    ID = 0x6fe1735b
    QUALNAME = "e2e.DecryptedMessageActionAcceptKey"

    def __init__(self, *, exchange_id: int, g_b: bytes, key_fingerprint: int) -> None:
        self.exchange_id = exchange_id  # long
        self.g_b = g_b  # bytes
        self.key_fingerprint = key_fingerprint  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessageActionAcceptKey":
        # No flags
        
        exchange_id = Long.read(b)
        
        g_b = Bytes.read(b)
        
        key_fingerprint = Long.read(b)
        
        return DecryptedMessageActionAcceptKey(exchange_id=exchange_id, g_b=g_b, key_fingerprint=key_fingerprint)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.exchange_id))
        
        b.write(Bytes(self.g_b))
        
        b.write(Long(self.key_fingerprint))
        
        return b.getvalue()
