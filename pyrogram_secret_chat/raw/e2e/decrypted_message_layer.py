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


class DecryptedMessageLayer(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``None``
        - ID: ``1BE31789``

    Parameters:
        random_bytes: ``bytes``
        layer: ``int`` ``32-bit``
        in_seq_no: ``int`` ``32-bit``
        out_seq_no: ``int`` ``32-bit``
        message: :obj:`DecryptedMessage <pyrogram_secret_chat.raw.base.DecryptedMessage>`
    """

    __slots__: List[str] = ["random_bytes", "layer", "in_seq_no", "out_seq_no", "message"]

    ID = 0x1be31789
    QUALNAME = "e2e.DecryptedMessageLayer"

    def __init__(self, *, random_bytes: bytes, layer: int, in_seq_no: int, out_seq_no: int, message: "raw.base.DecryptedMessage") -> None:
        self.random_bytes = random_bytes  # bytes
        self.layer = layer  # int
        self.in_seq_no = in_seq_no  # int
        self.out_seq_no = out_seq_no  # int
        self.message = message  # DecryptedMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DecryptedMessageLayer":
        # No flags
        
        random_bytes = Bytes.read(b)
        
        layer = Int.read(b)
        
        in_seq_no = Int.read(b)
        
        out_seq_no = Int.read(b)
        
        message = TLObject.read(b)
        
        return DecryptedMessageLayer(random_bytes=random_bytes, layer=layer, in_seq_no=in_seq_no, out_seq_no=out_seq_no, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.random_bytes))
        
        b.write(Int(self.layer))
        
        b.write(Int(self.in_seq_no))
        
        b.write(Int(self.out_seq_no))
        
        b.write(self.message.write())
        
        return b.getvalue()
