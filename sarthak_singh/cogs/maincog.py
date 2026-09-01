from discord.ext import commands
from discord import app_commands
import discord

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="start")
    @app_commands.describe(gangster_name="Your gangster name", gang_name="Your gang name")
    async def start(self, interaction: discord.Interaction, gangster_name: str, gang_name: str):
        await interaction.response.send_message(f"Don {gangster_name} sends his regards from {gang_name}.")

async def setup(bot):
    await bot.add_cog(MainCog(bot))