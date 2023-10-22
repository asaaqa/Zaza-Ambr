# ported from uniborg
# https://github.com/muhammedfurkan/UniBorg/blob/master/stdplugins/ezanvakti.py

import json

import requests

from ambro import CMD_HANDLER as cmd
from ambro import CMD_HELP
from ambro.modules.sql_helper.globals import gvarstatus
from ambro.utils import edit_delete, edit_or_reply, joo_cmd


@joo_cmd(pattern="اذان(?:\\s|$)([\\s\\S]*)")
async def get_adzan(adzan):
    "Shows you the Islamic prayer times of the given city name"
    input_str = adzan.pattern_match.group(1)
    LOKASI = gvarstatus(
        "WEATHER_DEFCITY") or "Jakarta" if not input_str else input_str
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        return await edit_delete(
            adzan, f"**Tidak Dapat Menemukan Kota** `{LOCATION}`", 120
        )
    result = json.loads(request.text)
    catresult = f"<b>مواقيت الصلوات الخمس:</b>\
            \n<b>📆 تاريخ </b><code>{result['items'][0]['date_for']}</code>\
            \n<b>📍 مدينه</b> <code>{result['query']}</code> | <code>{result['country']}</code>\
            \n\n<b>الفجر  : </b><code>{result['items'][0]['shurooq']}</code>\
            \n<b>الصباح : </b><code>{result['items'][0]['fajr']}</code>\
            \n<b>الضهر  : </b><code>{result['items'][0]['dhuhr']}</code>\
            \n<b>العصر  : </b><code>{result['items'][0]['asr']}</code>\
            \n<b>المغرب : </b><code>{result['items'][0]['maghrib']}</code>\
            \n<b>العشاء : </b><code>{result['items'][0]['isha']}</code>\
    "
    await edit_or_reply(adzan, catresult, "html")


CMD_HELP.update(
    {
        "اذان": f"**الامر : **`اذان`\
        \n\n  •  **Syntax :** `{cmd}adzan` <nama kota>\
        \n  •  **Function : **Menunjukkan waktu jadwal sholat dari kota yang diberikan.\
    "
    }
)
