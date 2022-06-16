import asyncio
from pyrogram import Client
from config import *
import libtorrent as lt


app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
  )

print("[INFO]: STARTING Lib Torrent CLIENT")
ses = lt.session()
ses.listen_on(6881, 6891)

queue = []