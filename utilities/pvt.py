import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command('start'))
async def startc(message):
  god = int(os.environ.get('OWNER_ID'))
  god_username = os.environ.get('OWNER_USERNAME')
  START_PM = '''
**Hey!!**
__I'm anti anonymous bot__,
I can kick the user who is sending msg anonymously in the chat'''
  START_BUT = [
    [
      InlineKeyboardButton('🗿 Summon me in chat', url='')
    ]
  ]
  await message.reply_text(
    text=START_PM,
    reply_markup=InlineKeyboardMarkup(START_BUT),
  )