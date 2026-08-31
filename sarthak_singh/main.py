import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency*1000)}ms")

@bot.tree.command(name="start")
@app_commands.describe(gangster_name="Your gangster name", gang_name="Your gang name")
async def start(interaction: discord.Interaction, gangster_name: str, gang_name: str):
    await interaction.response.send_message(f"Don {gangster_name} sends his regards from {gang_name}.")


bot.run(TOKEN)
