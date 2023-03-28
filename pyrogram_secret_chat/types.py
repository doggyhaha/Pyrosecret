from .raw.e2e import DecryptedMessage, DecryptedMessage8, DecryptedMessage23, DecryptedMessage46
from typing import Union, Any
from dataclasses import dataclass
from pyrogram.raw.types import UpdateNewEncryptedMessage

DECRYPTEDMESSAGES = (
    DecryptedMessage, 
    DecryptedMessage8, 
    DecryptedMessage23, 
    DecryptedMessage46
    )

@dataclass
class SecretMessage:
    raw: Union[DecryptedMessage, DecryptedMessage8, DecryptedMessage23, DecryptedMessage46]
    file: Any

class SecretEvent:
    def __init__(self, 
        methods, 
        base_update: UpdateNewEncryptedMessage, 
        decrypted_event: SecretMessage
    ) -> None:
        self.methods = methods
        self.base_update = base_update
        self.decrypted_event = decrypted_event

    async def reply(self, message: str, ttl: int = 0):
        return await self.methods.send_secret_message(self.base_update.message.chat_id, message, ttl,
                                            self.decrypted_event.raw.random_id)

    async def respond(self, message: str, ttl: int = 0):
        return await self.methods.send_secret_message(self.base_update.message.chat_id, message, ttl)