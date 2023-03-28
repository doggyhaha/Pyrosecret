import sqlite3
from enum import Enum
from typing import Callable
import logging

#from telethon import TelegramClient
#from telethon.sessions import SQLiteSession
#from telethon.tl import types
#from telethon.tl.alltlobjects import tlobjects
from pyrogram.client import Client
from pyrogram.handlers.raw_update_handler import RawUpdateHandler
from pyrogram.storage.sqlite_storage import SQLiteStorage
from pyrogram.raw.all import objects
from .raw.all import objects as newobjects
from pyrogram.raw.types.encrypted_chat import EncryptedChat
from pyrogram.raw.types.update_encryption import UpdateEncryption
from pyrogram.raw.types.encrypted_chat_requested import EncryptedChatRequested
from pyrogram.raw.types.update_new_encrypted_message import UpdateNewEncryptedMessage

from .storage.abstract import SecretSession
from .storage.sqlite import SecretSQLiteSession
from .storage.memory import SecretMemorySession
from .secret_methods import SecretChatMethods
from .types import SecretEvent

class SECRET_TYPES(Enum):
    accept = 1
    decrypt = 2


def patch_tlobjects():
    objects.update(newobjects)
    pass

class SecretChatManager(SecretChatMethods):

    def __init__(self, client: Client, session: SecretSession = None, auto_accept: bool = False,
                 new_chat_created: callable = None):
        self.secret_events = []
        self.dh_config = None
        self.dh_prime = None
        self.auto_accept = auto_accept
        self.client = client
        self.new_chat_created = new_chat_created
        self._log = logging.getLogger('secretchats')
        if not session:
            self.session = SecretMemorySession()
        elif isinstance(session, sqlite3.Connection):
            self.session = SecretSQLiteSession(session)
        elif isinstance(session, SQLiteStorage):
            self.session = SecretSQLiteSession(session._conn)
        else:
            self.session = session
        self.client.add_handler(RawUpdateHandler(self._secret_chat_event_loop))
        #self._log = client._log["secret_chat"]

    def add_secret_event_handler(self, event_type=SECRET_TYPES.decrypt, func: Callable = None):
        if event_type not in (SECRET_TYPES.decrypt, SECRET_TYPES.accept) or not func:
            raise ValueError("Wrong params")
        # deal with patterns etc
        print("SECRETO")
        self.secret_events.append((event_type, func))
        print(self.secret_events)

    def patch_event(self, event, decrypted_event):
        print(decrypted_event)
        event = SecretEvent(self, event, decrypted_event)
        return event

    async def _secret_chat_event_loop(self, cl, event, users, chats):
        if 0x1be31789 not in objects:  # check for DecryptedMessageLayer constructor
            patch_tlobjects()  # patch the tlobjects so we can read it with bytes

        if isinstance(event, UpdateEncryption):
            if isinstance(event.chat, EncryptedChat):

                await self.finish_secret_chat_creation(event.chat)
                if self.new_chat_created:
                    self.client.loop.create_task(self.new_chat_created(event.chat,created_by_me=True))
            elif isinstance(event.chat, EncryptedChatRequested):
                if self.auto_accept:
                    await self.accept_secret_chat(event.chat)
                    if self.new_chat_created:
                        self.client.loop.create_task(self.new_chat_created(event.chat, created_by_me=False))
                    return
                for events in self.secret_events:
                    (event_type, callback) = events
                    if event_type == SECRET_TYPES.accept:
                        self.client.loop.create_task(callback(event))
        elif isinstance(event, UpdateNewEncryptedMessage):
            decrypted_event = None
            for events in self.secret_events:
                (event_type, callback) = events
                if event_type == SECRET_TYPES.decrypt:
                    print("event decrypt")
                    if not decrypted_event:
                        print("not decrypted")
                        decrypted_event = await self.handle_encrypted_update(event)
                        if "SecretMessage" not in type(decrypted_event).__name__:
                            print("LINEA 99")
                            print(type(decrypted_event).__name__)
                            return

                        event = self.patch_event(event, decrypted_event)
                        print("evento patchat")
                    print("io avrei chiamato e")
                    self.client.loop.create_task(callback(event))
