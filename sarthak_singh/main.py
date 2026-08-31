import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency*1000)}ms")

bot.run(TOKEN)
