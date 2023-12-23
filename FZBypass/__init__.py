from os import getenv
from time import time
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.enums import ParseMode
from logging import getLogger, FileHandler, StreamHandler, INFO, ERROR, basicConfig
from uvloop import install

install()
basicConfig(format="[%(asctime)s] [%(levelname)s] - %(message)s", #  [%(filename)s:%(lineno)d]
            datefmt="%d-%b-%y %I:%M:%S %p",
            handlers=[FileHandler('log.txt'), StreamHandler()],
            level=INFO)

getLogger("pyrogram").setLevel(ERROR)
LOGGER = getLogger(__name__)

load_dotenv('config.env', override=True)
BOT_START = time()

class Config:
    BOT_TOKEN = ('6440302815:AAH2-6t-dxB74lMmg0aY5tl35kP_Rry9cPA')
    API_HASH  = ('b36c5dc986f77eedd4bbf356b65eab19')
    API_ID    = ('21027612')
    if BOT_TOKEN == '' or API_HASH == '' or API_ID == '':
        LOGGER.critical('ENV Missing. Exiting Now...')
        exit(1)
    AUTO_BYPASS     = getenv('AUTO_BYPASS', 'False').lower() == 'true'
    AUTH_CHATS = ('-1002005718645')
    OWNER_ID        = int(getenv('OWNER_ID', 0))        
    DIRECT_INDEX    = getenv('DIRECT_INDEX', '').rstrip('/')
    LARAVEL_SESSION = getenv('LARAVEL_SESSION', '')
    XSRF_TOKEN      = getenv('XSRF_TOKEN', '')
    GDTOT_CRYPT     = getenv('GDTOT_CRYPT', '')
    DRIVEFIRE_CRYPT = getenv('DRIVEFIRE_CRYPT', '')
    HUBDRIVE_CRYPT  = getenv('HUBDRIVE_CRYPT', '')
    KATDRIVE_CRYPT  = getenv('KATDRIVE_CRYPT', '')
    UPTOBOX_TOKEN   = getenv('UPTOBOX_TOKEN', '')
    TERA_COOKIE     = getenv('TERA_COOKIE', '')

Bypass = Client("FZ", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN, plugins=dict(root="FZBypass/plugins"), parse_mode=ParseMode.HTML)
