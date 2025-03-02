

import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7869629794:AAHDFgaViacFBaJWYgDYeT1Qgrcz06qWsg8")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27705761"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "822cb334ca4527a134aae97f9fe44fd6")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002397556354"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "6987158459")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6987158459"))

#Port
PORT = os.environ.get("PORT", "8443")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://akashz9t:asdfg@cluster0.zu0io.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002004115638"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002475067865"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "50"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>›› Hᴇʏ {first} ×</blockquote>     ɪ ᴀᴍ ᴀ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴀɴɪᴍᴇxɢᴀʟʟᴇʀʏ ⚡.</b>")
try:
    ADMINS=[6987158459]
    for x in (os.environ.get("ADMINS", "6987158459").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b><blockquote>›› Hᴇʏ {mention} ×</blockquote>      ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, ᴊᴏɪɴ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>\n›› 𝖡ʏ <a href='https://t.me/animexgallery'>ᴀɴɪᴍᴇxɢᴀʟʟᴇʀʏ</a></b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b></b>"

ADMINS.append(OWNER_ID)
ADMINS.append(6987158459)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
