import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command('start'))
async def startc(message, m):
  #god = int(os.environ.get('OWNER_ID'))
  #god_username = os.environ.get('OWNER_USERNAME')
  START_PM = '''
**Hey!!**
__I'm anti anonymous bot__,
I can kick the user who is sending msg anonymously in the chat'''
  START_BUT = [
    [
      InlineKeyboardButton('🗿 Summon me in chat', url='')
    ]
  ]
  await Client.reply_text(
    text=START_PM,
    reply_markup=InlineKeyboardMarkup(START_BUT),
  )

@Client.on_message(filters.private & filters.incoming)
async def ohk(message, m):
  user = m.from_user.id
  if Client.sender_chat:
    await Client.reply_text(
      text=f'**Banning** ({user})\n\n**Reason: `It was an channel`'
    )
    await m.chat.ban_member(user)
      
