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


class DecryptedMessageService8(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``AA48327D``

    Parameters:
        random_id: ``int`` ``64-bit``
        random_bytes: ``bytes``
        action: :obj:`DecryptedMessageAction <pyrogram_secret_chat.raw.base.DecryptedMessageAction>`
    """

    __slots__: List[str] = ["random_id", "random_bytes", "action"]

    ID = 0xaa48327d
    QUALNAME = "e2e.DecryptedMessageService8"

    def __init__(self, *, random_id: int, random_bytes: bytes, action: "raw.base.DecryptedMessageAction") -> None:
        self.random_id = random_id  # long
        self.random_bytes = random_bytes  # bytes
        self.action = action  # DecryptedMessageAction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessageService8":
        # No flags
        
        random_id = Long.read(b)
        
        random_bytes = Bytes.read(b)
        
        action = TLObject.read(b)
        
        return DecryptedMessageService8(random_id=random_id, random_bytes=random_bytes, action=action)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.random_id))
        
        b.write(Bytes(self.random_bytes))
        
        b.write(self.action.write())
        
        return b.getvalue()
