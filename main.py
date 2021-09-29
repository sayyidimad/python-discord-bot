from tools.kanji import kanji
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

@bot.command(description="ini adalah deskripsi tambahan")
async def add(ctx, left: int, right: int):
    """Menjumlahkan 2 bilangan."""
    await ctx.send(left + right)

@bot.command()
async def translate(ctx, word: str):
    """Menterjemahkan kata menjadi Kanji Jepang."""
    await ctx.send(kanji.search(word))

# Memulai bot
bot.run(os.environ['TOKEN'])