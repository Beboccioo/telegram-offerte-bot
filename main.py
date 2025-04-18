from telethon import TelegramClient, events
import re
import asyncio

api_id = 21881791
api_hash = '020bd1e1a42ffc15a9409d9bf280c1e3'
source_channel = 'offertepuntotech'
target_channel = 'sconti_amazonit'

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    msg = event.message.message

    # Modifica link Amazon per aggiungere tag affiliato
    modified_msg = re.sub(
        r'(https://www\\.amazon\\.it/[^\\s?]+)(\\?[^\\s]*)?',
        lambda m: m.group(1) + '?tag=offerte069-21',
        msg
    )

    await client.send_message(target_channel, modified_msg)

client.start()
client.run_until_disconnected()
