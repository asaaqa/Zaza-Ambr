#    TeleBot - ambro
#    Copyright (C) 2020 TeleBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#    Recode by Fariz <Github.com/farizjs>
#    From Flicks-ambro
#    <t.me/TheFlicksambro>


from ambro import BOT_USERNAME, CMD_HELP, bot
from ambro.utils import edit_or_reply, edit_delete, joo_cmd

user = bot.get_me()
DEFAULTUSER = user.first_name
CUSTOM_HELP_EMOJI = "ރ"


@joo_cmd(pattern="مساعده(.*)")
async def cmd_list(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, f"**ރ Commands Available In {args} ރ** \n\n" + str(CMD_HELP[args]) + "\n\n**☞ @ProjectJoni**")
        else:
            await edit_delete(event, f"**Module** `{args}` **Tidak Tersedia!**")
    else:
        try:
            results = await bot.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "@smauabot"
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except BaseException:
            await edit_delete(event,
                              f"** Sepertinya obrolan atau bot ini tidak mendukung inline mode.**"
                              )
