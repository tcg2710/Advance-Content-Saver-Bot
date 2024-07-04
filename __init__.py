#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("18688563", default=None, cast=int)
API_HASH = config("48315c25585c23eee6b1f346aad17a68", default=None)
BOT_TOKEN = config("6786278075:AAHvQDFYEUk68NtJ95uAHyLKCC02afDLjpo", default=None)
SESSION = config("BQCTxF_JKRSCREkZLNiVLfFyERGYvqML1dEu95KHqbHgNSCzDV_RqcjEV9iE6Z68ZjjdwEj0dZfinpod4yEKM2uXgjntZ56qY5rkGRZYN5tv4Ul-SQOUVyQQWdWRKjVUNZWNLTEzt1AoMkrB3WcsMfzL1FChNYhRPsQpaqPhAmsFJ_ZNE5psZ32GPm9ro566c2jYdrzfd74HNUHM08uHrq1SBS7Q9ktmTUkE26558qQwEMki8X6MPLmjf28hf7OYdXnbCLj1H2HIiwb2sAra9dbT3QmNa9K9kDCY6F36zFUtIKEG3tpG94zVvwQ8r_MAUaQCx_CtIL0Wi0rsyq-oOqn_AAAAAUuSxxUA", default=None)
FORCESUB = config("dndmovie", default=None)
AUTH = config("5562877717", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
