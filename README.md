# PyroSecret 🔐

Primitive unstable and incomplete Python library to work with Telegram's Secret Chats based on [Pyrogram](httpa://github.com/pyrogram/pyrogram).  

This library was just a test of mine, i don't even remember if it works 💀.  

> **Note**
> This library is not maintained anymore, it was made for personal use and is not production ready.

This project is basically derived from [painor/telethon-secret-chat](https://github.com/painor/telethon-secret-chat) and [Telegram's docs](https://core.telegram.org/api/end-to-end).

The e2e schema is taken from [tdlib](https://github.com/tdlib/td/blob/master/td/generate/scheme/secret_api.tl).

I don't know if this library is even useful, but i'm sharing it anyway.

> **Warning**
> This library is not stable, it may not work at all, i can't guarantee its security, some pre-generated raw methods are already provided because the generator is pretty broken.

## Installation

```bash
git clone https://github.com/doggyhaah/pyrosecret
cd pyrosecret
pip install .
```

## Usage

```python
from pyrogram import Client
from pyrogram_secret_chat import SecretChatManager
from pyrogram_secret_chat.types import SecretEvent
import logging
from io import BytesIO
from pyrogram_secret_chat.raw.e2e import DecryptedMessageMediaPhoto
from pyrogram_secret_chat import save_photo

client = Client("prod2", test_mode=False, api_id=123456, api_hash='yourapihash')

ids = []

async def replier(event: SecretEvent):
    print(event)
    print("event received")
    if event.decrypted_event.raw.message:
        if event.base_update.message.chat_id not in ids:
            ids.append(event.base_update.message.chat_id)
            await event.reply("Hello there!")
        else:
            await event.reply(event.decrypted_event.raw.message) # parse_mode is markdown by default
    else:
        if event.decrypted_event.raw.media and isinstance(event.decrypted_event.raw.media, DecryptedMessageMediaPhoto):
            bio = BytesIO()
            media = event.decrypted_event.raw.media
            save_photo(event.decrypted_event, bio)
            sc = manager.get_secret_chat(event.base_update.message.chat_id)
            await manager.send_secret_photo(sc, bio, bio, media.thumb_w, media.thumb_h, media.w, media.h, media.size, media.caption)


async def new_chat(chat, created_by_me):
    if created_by_me:
        print("User {} has accepted our secret chat request".format(chat))
    else:
        t = "nuova chat top secret {}".format(chat)
        print(t)
        await client.send_message("me", t)
        await client.send_message("me", "admin id: {}".format(chat.admin_id))

log = logging.getLogger('secretchats')
log.setLevel(logging.DEBUG)

manager = SecretChatManager(client, auto_accept=True,
new_chat_created=new_chat)  # automatically accept new secret chats
manager.add_secret_event_handler(func=replier)  # we can specify the type of the event

client.run()
```


> **Note**
> Due to the fact that secret chats are end-to-end encrypted, if the user tries to accept a secret chat which was already accepted from another session (for example if the user is online from an official client).


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

Everyone is welcome to contribute to this project maybe even continuing it.
