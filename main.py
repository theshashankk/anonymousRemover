import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyrogram import Client 
logging.getLogger("pyrogram").setLevel(logging.WARNING)

API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = os.environ.get('API_HASH')

if __name__ == "__main__" :
    plugins = dict(
        root="utilities"
    )
    app = Client(
        "Anonymous",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins,
        workers=100
    )
    app.run()
