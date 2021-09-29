from tools.kanji import kanji
import discord
import logging
import os

# Inisialisasi Discord API
client = discord.Client()

# Inisialisasi Logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Fungsi yang akan dijalankan ketika bot berjalan
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Fungsi yang akan dijalankan ketika terdapat pesan yang masuk
@client.event
async def on_message(message):
    msg = message.content

    if message.author == client.user:
        pass

    if msg.startswith('Robot-kun, translate'):
        word = msg.split("Robot-kun, translate ", 1)[1]
        print(word)
        word = kanji.search(word)

        await message.channel.send(word)

# Memulai bot
client.run(os.environ['TOKEN'])