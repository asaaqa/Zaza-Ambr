# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" ambro start point """

import sys
from importlib import import_module

import requests
from telethon.tl.functions.channels import InviteToChannelRequest as Addbot
from ambro import (
    BOTLOG_CHATID,
    BOT_USERNAME,
    BOT_TOKEN,
    BOT_VER,
    ALIVE_LOGO,
    LOGS,
    kyyblacklist,
    bot,
    call_py,
)
from ambro.modules import ALL_MODULES
from ambro import CMD_HANDLER as cmd
from ambro.utils import autobot, autopilot

try:
    bot.start()
    call_py.start()
    user = bot.get_me()
    kyyblacklist = requests.get(
        "https://raw.githubusercontent.com/muhammadrizky16/Kyyblack/master/kyyblacklist.json"
    ).json()
    if user.id in kyyblacklist:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, ambronya GUA MATIIN NAJIS BANGET DIPAKE ORANG KEK LU.\nCredits: @ikhsanntarjo"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("ambro.modules." + module_name)

if not BOTLOG_CHATID:
    LOGS.info(
        "BOTLOG_CHATID Vars tidak terisi, Memulai Membuat Grup Otomatis..."
    )
    bot.loop.run_until_complete(autopilot())

LOGS.info(
    f"Jika {user.first_name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/JoniSupport")
LOGS.info(
    f"🥷 ѕᴏʀᴄᴇ ᴀᴍʙʀᴏ 🥷 ⚙️ V{BOT_VER} [TELAH DIAKTIFKAN!]")


async def check_alive():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_file(BOTLOG_CHATID, ALIVE_LOGO, caption=f"✨**Joo-ambro Berhasil Diaktifkan**!!\n━━━━━━━━━━━━━━━\n➠ **ambro Version** - `3.1.5@Joo-ambro`\n➠ **Ketik** `{cmd}help` **Untuk Mengecheck Bot**\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @ProjectJoni ")
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass

bot.loop.run_until_complete(check_alive())
if not BOT_TOKEN:
    LOGS.info(
        "BOT_TOKEN Vars Tidak Terisi, Memulai Membuat BOT Otomatis Di @Botfather..."
    )
    bot.loop.run_until_complete(autobot())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
