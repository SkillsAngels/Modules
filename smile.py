__version__ = (1, 0, 0)
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

from .. import loader, utils

import asyncio
from telethon.tl.types import Message


@loader.tds
class Smile(loader.Module):

    strings = {"name": "Smile"}

    async def heartscmd(self, message: Message):
        for _ in range(10):
            for heart in {"🤍", "🤎", "❤️", "💙", "💛", "💜", "🖤"}:
                message = await utils.answer(message, heart)
                await asyncio.sleep(0.4)

    async def mooncmd(self, message: Message):
        for _ in range(10):
            for moon in ["🌝", "🌚"]:
                message = await utils.answer(message, moon)
                await asyncio.sleep(0.4)
