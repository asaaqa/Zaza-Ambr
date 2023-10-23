import sys

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

from .bothseesion import bothseesion
from .client import AmbUserBotClient
from .logger import logging

LOGS = logging.getLogger("أمبرو")
__version__ = "2.10.6"

loop = None

if Config.STRING_SESSION:
    session = bothseesion(Config.STRING_SESSION, LOGS)
else:
    session = "ambro"

try:
    ambub = AmbUserBotClient(
        session=session,
        api_id=Config.API_KEY,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(
        f"STRING_SESSION CODE WRONG MAKE A NEW SESSION - {e}\n كود سيشن تيليثـون غير صالح .. قم باستخـراج كود جديد ؟!"
    )
    sys.exit()

try:
    ambub.tgbot = tgbot = AmbUserBotClient(
        session="ambTgbot",
        api_id=Config.API_KEY,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=Config.BOT_TOKEN)
except AccessTokenExpiredError:
    LOGS.error("توكن البوت غير صالح قم باستبداله بتوكن جديد من بوت فاذر")
except AccessTokenInvalidError:
    LOGS.error("توكن البوت غير صحيح قم باستبداله بتوكن جديد من بوت فاذر")
