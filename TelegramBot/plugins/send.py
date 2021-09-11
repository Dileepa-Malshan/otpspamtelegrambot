from .. import bot
from telethon import events
import requests
from config import vars
import time,os
try:
    from requests import post,get


def send_message(number):
    base_url = 'https://guru.lk/auth/headstart/ajax.php'
    params = {
        'phone':number,'course':'1','sesskey':'','action':'sms_reg'
            }
   @bot.on(events.NewMessage(pattern='/send$', func=lambda e: e.is_private))
async def send(event):
    async with bot.conversation(await event.get_chat(), exclusive=False, total_timeout=600) as conv:
        await conv.send_message("Send me SRILANKA 🇮🇳 number without +94 in 60 seconds.")
        phone_number = await conv.get_response(timeout=(60))      
        sms_resp, status_code = send_message(phone_number.text,  message.text)
        await conv.send_message(f"**Response from API** : `{sms_resp}`.\n**Status code** : `{status_code}`\nThanks for using this bot.")

