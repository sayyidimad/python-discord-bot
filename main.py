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
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
async def on_ready():
    # Fungsi yang akan dijalankan ketika bot berjalan
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def sincostan(ctx, jenis="sin", depan=0, miring=0, samping=0):
    """
    argumen ctx berarti context, channel yg digunakan saat bot dipanggil
    argumen depan menerima nilai angka sudut depan
    argumen miring menerima nilai angka sudut miring
    argumen samping menerima nilai angka sudut samping
    Menemukan hasil sudut sin cos tan.
    """

    result = 0
    if jenis == "sin":
        result = depan / miring

    elif jenis == "cos":
        result = samping / miring

    elif jenis == "tan":
        result = depan / samping

    await ctx.send(result)


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
