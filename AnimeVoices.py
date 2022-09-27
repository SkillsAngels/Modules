
#        ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#        █▀█ █░▀░█ █▄█ █▀▄ ██▄
#
#                 © Copyright 2022
#
#          https://t.me/the_farkhodov
# _           _            _ _
# | |         | |          (_) |
# | |     _ | |_ _  _ _| | 
# | |    / _ \| / _ \/ | | |/ /
# | |_| (_) | || (_) \ \ |   <
# \_/\_/ \\_/|_/_|_|\_\
#
#              © Copyright 2022
#
#         developed by @lotosiiik, @byateblan
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_only
# scope: hikka_min 1.3.3
# meta developer: @amoremods @hikkaftgmods
# meta banner: https://ibb.co/3NjJHvv
# meta pic: https://ibb.co/zX25RNd

from .. import loader


@loader.tds
class AnimeVoicesMod(loader.Module):
    """🎤 Popular Anime Voices"""

    strings = {"name": "AnimeVoices"}

    async def smexkcmd(self, message):
        """Смех Канеки"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/25",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def smexycmd(self, message):
        """Смех Ягами"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/101",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def znaycmd(self, message):
        """Знай свое место ничтожество"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/27",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def madaracmd(self, message):
        """Учиха Мадара"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/28",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def sharingancmd(self, message):
        """Итачи Шаринган"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/29",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def imsasukecmd(self, message):
        """Учиха Саске"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/30",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def paincmd(self, message):
        """Познайте боль"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/74",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def rascmd(self, message):
        """Расширение территории"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/81",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def tenseicmd(self, message):
        """Shinra tensei"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/82",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def dazaicmd(self, message):
        """Дазаи"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/83",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def gaycmd(self, message):
        """I'm gay"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/84",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def bankaicmd(self, message):
        """Bankai"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/85",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def satecmd(self, message):
        """Sate sate sate"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/86",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def yoaimocmd(self, message):
        """Yoaimo"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/87",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def madaracmd(self, message):
        """Он один из основателей конохи"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/91",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def valhallacmd(self, message):
        """У нас будет крутейшая байкерская банда в Канто."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/92",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def itachicmd(self, message):
        """В возрасте 7 лет он уже мыслил как Хокаге."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/93",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ghoulcmd(self, message):
        """Я...Гуль."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/94",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def bestcmd(self, message):
        """В общем раз уж я сдесь стану лучшим.(Повар боец Сомо)"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/95",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def requiemcmd(self, message):
        """Это реквием."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/96",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def kingcmd(self, message):
        """Король вернулся."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/97",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def equalitycmd(self, message):
        """цитата Аянокоджи про равенство."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/98",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def forestcmd(self, message):
        """Нельзя понять всю красоту леса оценивая лишь одно дерево."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/99",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def bankaiichigocmd(self, message):
        """Банкай Ичиго."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/VoiceAmore/100",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
