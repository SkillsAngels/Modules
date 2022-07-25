__version__ = (0, 0, 1)

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
# meta banner: https://i.imgur.com/2KZ38Pv.jpeg
# meta pic: https://i.imgur.com/QntqxyH.jpeg

import logging
import re
import asyncio
from .. import loader, utils


logger = logging.getLogger(__name__)


@loader.tds
class IrisLabMod(loader.Module):
    """Модуль который показывает лаб/жертв(в целом бесполезный модуль)
    p.s в этом модуле возможны задержки на получение инфы сорян"""

    strings = {
        "name": "IrisLab",
        "lab_data": {
            "d": "(.*) Досье лаборатории (.*)",
            "s": "(.*) Руководитель: (.*)",
            "с": "(.*) В составе Корпорации (.*)",
            "n": "(.*) Имя патогена: (.*)",
            "p": "(.*) Готовых патогенов: (.*) из (.*)",
            "q": "(.*) Квалификация учёных: (.*)",
            "np": "(.*) Новый патоген: (.*)",
            "inf": "(.*) Заразность: (.*)",
            "imn": "(.*) Иммунитет: (.*)",
            "m": "(.*) Летальность: (.*)",
            "ss": "(.*) Служба безопасности: (.*)",
            "be": "(.*) Био-опыт: (.*)",
            "br": "(.*) Био-ресурс: (.*)",
            "so": "(.*) Спецопераций: (.*)",
            "prev": "(.*) Предотвращены: (.*)",
            "i": "(.*) Заражённых: (.*)",
            "dis": "(.*) Своих болезней: (.*)",
            "f": "<b> Руководитель в состоянии горячки",
        },
    }

    async def client_ready(self, client, db):
        db.set("Iris", "chat_biowar", 707693258)

        self.client = client
        self.db = db

    async def message_q(
        self,
        text: str,
        user_id: int,
        mark_read: bool = False,
        delete: bool = False,
    ):
        """Отправляет сообщение и возращает ответ"""
        async with self.client.conversation(user_id) as conv:
            msg = await conv.send_message(text)
            response = await conv.get_response()
            if mark_read:
                await conv.mark_read()

            if delete:
                await msg.delete()
                await response.delete()

            return response

    async def labcmd(self, message):
        """Модуль который выдаст вам статистику вашей лаборатории (лаб)"""
        lab = await self.message_q(".Лаб", 707693258, mark_read=True, delete=True)
        args_raw = utils.get_args_raw(message)
        if not args_raw:
            return await utils.answer(message, lab.text)

        data, text = self.strings("lab_data"), []
        flags = "".join(args_raw.split(" ")).split("-")
        if "" in flags:
            flags.remove("")
        for flag in flags:
            search = re.search(data[flag], lab.text) if flag in data else None
            if search:
                if flag == "be":
                    num = search.group().split(":")[-1].replace(" ", "")
                    if num[-1] == "k":
                        num = (
                            int(num[:-1].replace(",", "")) * 100 / 100 * 10
                            if "," in num
                            else int(num[:-1]) * 1000 / 100 * 10
                        )
                    elif num[:-1] != "k":
                        num = int(num) / 100 * 10
                    text.append(f"{search.group()} | {num}")
                elif flag == "d":
                    text.append(search.group()[:-1])
                else:
                    text.append(search.group())
            elif flag == "parametrs":
                text = """
d: Имя лаборатории
s: Руководитель
с: Корпорация

n: Имя патогена
p: Готовых патогенов
q: Квалификация учёных 👨‍🔬
np: Новый патоген через... ⏱

inf: Заразность 
imn: Иммунитет 🛡️
m: Летальность ☠️
ss: Служба безопасности 

be: Био-опыт ☣️
br: Био-ресурс 🧬
so: Спецопераций 😷
prev: Предотвращены 🥽

i: заражённых 🤒
dis: Своих болезней 🤒

f: Горячка руководителя 
v: Ежедневная премия(ежа) 💸"""
                return await utils.answer(
                        message,
                        text
                    )
            elif flag == "v":
                    await asyncio.sleep(3)
                    victims = await self.message_q("Мои жертвы", 707693258, mark_read=True, delete=True)
                    pattern = r"""(.*) Ежедневная премия: (.*)"""
                    result = re.search(pattern, victims.text).group()
                    text.append(result)
            else:
                    if flag in data:
                        app_text = "✅ Все патогены приготовлены" if flag == "np" else "❌ Горячки нету"
                        text.append(app_text)
                    else:
                        text.append("Параметр -{} не указан.".format(
                            flag
                        ))
            return await utils.answer(
                message,
                "\n".join(text)
                )
    async def victimscmd(self, message):
        """Комманда показывает ваши жертвы"""
        victims = await self.message_q(
            "Мои жертвы",
            707693258,
            mark_read=True,
            delete=True,
        )

        args_raw = utils.get_args_raw(message)

        if not args_raw:
            await utils.answer(message, victims.text)

    async def upgcmd(self, message):
        """Увеличивает зз/имун и тд.Как использовать(Пример) .upg летальность (число 1-5)"""
        args = utils.get_args(message)
        characteristics = ("заразность", "летальность", "иммунитет",
                            "безопасность", "разработка", "патогены")
        if not len(args) == 2:
            await utils.answer(
            message,
            "Указано больше или меньше двух параметров")
        elif args[0].lower() not in characteristics:
            await utils.answer(
            message,
            "Данного улучшения не существует")
        elif not args[1].isdigit():
            await utils.answer(
            message,
            "Второй параметр не является числом")
        elif int(args[1]) > 5 or int(args[1]) < 0:
            await utils.answer(
            message,
            "Уровень указан вне допустимого диапазона")
        else: await message.respond(f"++{args[0].lower()} {args[1]}")
