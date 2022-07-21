__version__ = (1, 0, 1)
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
# meta banner: https://i.imgur.com/Xzi8UL0.jpeg

from .. import loader, utils
import asyncio
from telethon.tl.types import Message


@loader.tds
class LoveMod(loader.Module):
    """Красивые слова для второй половинки"""

    strings = {"name": "Love"}

    async def lvgcmd(self, message: Message):
        """Активирует красивые слова для девушки"""

        for i, sentence in enumerate(
            [
                "❤️ | Пожалуйста солнце читай до конца!!",
                "❤️ | ......",
                "❤️ | Ты самая лучшая.",
                "❤️ | Самая милая.",
                "❤️ | Самая прекрасная.",
                "❤️ | Неповторимая",
                "❤️ | Идеальная",
                "❤️ | Умная",
                "❤️ | Незабываемая ",
                "❤️ | И вообще, ты мое солнце.",
                "❤️ | Я Тебя Люблю ❤️",
            ]
        ):
            message = await utils.answer(message, f"{i} {sentence}")
            await asyncio.sleep(1)

    async def lvpcmd(self, message: Message):
        """Активирует красивые слова для парня"""

        for i, sentence in enumerate(
            [
                "❤️ | Пожалуйста Зайка читай до конца!!",
                "❤️ | ......",
                "❤️ | Ты самый лучший.",
                "❤️ | Самый милый.",
                "❤️ | Самый прекрасный.",
                "❤️ | Неповторимый",
                "❤️ | Идеальный",
                "❤️ | Умный",
                "❤️ | Незабываемый ",
                "❤️ | И вообще, ты мое счастье.",
                "❤️ | Я Тебя Люблю ❤️",
            ]
        ):
            message = await utils.answer(message, f"{i} {sentence}")
            await asyncio.sleep(1)
