#
# _           _            _ _
# | |         | |          (_) |
# | |     ___ | |_ ___  ___ _| | __
# | |    / _ \| __/ _ \/ __| | |/ /
# | |___| (_) | || (_) \__ \ |   <
# \_____/\___/ \__\___/|___/_|_|\_\
#
#              © Copyright 2022
#
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @hikkaftgmods
# meta banner: https://i.imgur.com/P3fguXK.jpeg
# meta icon: https://i.imgur.com/sWz2mob.jpeg

import io
from .. import loader, utils
from telethon.tl.types import Message


@loader.tds
class SDPicsMod(loader.Module):
    """Module to save self-destructing media"""

    strings = {
        "name": "SDPics",
        "usage": "🚫 <b>Please, reply to self-destructing media</b>",
    }

    strings_ru = {
        "usage": "🚫 <b>Пожалуйста, ответь на самоуничтожающееся фото</b>",
        "_cls_doc": "Модуль для сохранения самоуничтожающихся фото",
        "_cmd_doc_s": "<Реплай на самоуничтожающееся фото>",
    }

    async def scmd(self, message: Message):
        """<reply to self-destructing media>"""
        reply = await message.get_reply_message()
        if not reply or not reply.media.ttl_seconds:
            await utils.answer(message, self.strings("usage"))
            return

        await message.delete()
        file = io.BytesIO(await reply.download_media(bytes))
        file.name = reply.file.name
        await self._client.send_file("me", file)