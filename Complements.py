__version__ = (0, 0, 1)
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
#         developed by @lotosiiik, @byateblan
#
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @hikkaftgmods
# meta banner: https://i.imgur.com/kDshq0N.jpeg
# meta pic: https://i.imgur.com/xC4oVi6.jpeg

from .. import loader, utils
import asyncio
from telethon.tl.types import Message


@loader.tds
class ComplementsMod(loader.Module):
    """Модуль который дарит комплементы девушке/парню"""

    strings = {"name": "Complements"}

    async def cgcmd(self, message: Message):
        """Эта команда дарит комплементы девушке"""

        for i in [
            "Пожалуйста прочти до конца",
            "......",
            "Ты прекрасна как всегда",
            "Ты просто неповторима",
            "Сногшебательна",
            "Идеальна",
            "Красива",
            "Умопомрачительна",
            "Незабываемая ",
            "Лучшая",
            "Маленькое солнышко",
            "Чудо",
        ]:
            message = await utils.answer(message, i)
            await asyncio.sleep(1)

    async def cbcmd(self, message: Message):
        """Эта команда дарит комплементы парню"""

        for i in [
            "Пожалуйста прочти до конца",
            "......",
            "Ты прекрасный как всегда",
            "Ты просто неповторимый",
            "Сногшебательный",
            "Идеальный",
            "Красивый",
            "Умопомрачительный",
            "Незабываемый",
            "Лучшый",
            "Маленькое солнышко",
            "Чудо",
        ]:
            message = await utils.answer(message, i)
            await asyncio.sleep(1)