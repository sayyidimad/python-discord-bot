import discord
import os
import requests
import json
import random

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
starter_encouragements = ["Daijoubu dayo!", "Yoshi yoshi, kimi wa yasashii ko da ne.", "Ganbatte"]

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

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        pass

    msg = message.content

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if msg.startswith('Robot-kun, translate'):
        word = msg.split("Robot-kun, translate ", 1)[1]
        print(word)

        kanji = get_kanji(word)

        await message.channel.send(kanji)

    # if msg.startswith('Robot-kun,'):
    #     await message.channel.send('はい')

client.run(os.getenv('TOKEN'))