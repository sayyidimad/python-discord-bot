from helper.VSBattles import VSBattles
from discord.ext import commands
import discord
import logging
import os

description = '''Bot ini dapat digunakan untuk mencari informasi character shounen.'''

# Inisialisasi Discord API
bot = commands.Bot(command_prefix='Robot-kun!', description=description)

# Inisialisasi Logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Fungsi yang akan dijalankan ketika bot berjalan
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def char(ctx, name: str):
    """Mendapatkan bio singkat dari karakter anime shounen."""
    character = VSBattles(name)
    embed = discord.Embed()

    embed.url = character.url
    embed.title = character.name
    embed.description = character.bio()
    embed.colour = discord.Colour.blue()

    embed.set_image(url=character.image())
    embed.set_footer(text=character.summary())

    await ctx.send(embed=embed)

# Memulai bot
bot.run(os.environ['TOKEN'])