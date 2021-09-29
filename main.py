import discord
import os
import requests
import json
import random

# Inisialisasi Discord API
client = discord.Client()

# Fungsi untuk menterjemahkan kata dari bahasa Inggris menjadi Jepang dengan KanjiAlive API
def get_kanji(word="see"):
    url = "https://kanjialive-api.p.rapidapi.com/api/public/search/advanced/"
    querystring = {"rem":word}
    headers = {
        'x-rapidapi-host': "kanjialive-api.p.rapidapi.com",
        'x-rapidapi-key': "cffe543a60msh7a6d9f78131a3a7p17436cjsnbc606a064d5f"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    kanji = json_data[0]["kanji"]["character"]

    return kanji

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
        kanji = get_kanji(word)

        await message.channel.send(kanji)

# Memulai bot
client.run(os.environ['TOKEN'])