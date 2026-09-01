from discord.ext import commands
from discord import app_commands
import discord
import asyncio
import random

gameData = {}

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="start")
    @app_commands.describe(gangster_name="Your gangster name", gang_name="Your gang name")
    async def start(self, interaction: discord.Interaction, gangster_name: str, gang_name: str):
        gameData[interaction.user.id] = {"gang": gang_name, "cash" : 10000, "muscle": 1}
        print(gameData)
        await interaction.response.send_message(f"Don {gangster_name} sends his regards from {gang_name}.")

    @commands.command(name="mug")
    async def mug(self, ctx):
        msg = await ctx.reply("Wait for the target to look away...")
        await asyncio.sleep(random.randint(2,6))
        await msg.edit(content="🚨 GO! REACT NOW!")
        await msg.add_reaction("👛")

        def check(reaction, user):
            return user == ctx.author and reaction.message.id == msg.id and str(reaction.emoji) == "👛"
        
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=2.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("You weren't fast enough")
        else:
            earned = random.randint(2,5)*100
            gameData[ctx.author.id]["cash"] += earned
            await ctx.send(f"You successfully stole {earned}, your current balance is {gameData[ctx.author.id]["cash"]}")



async def setup(bot):
    await bot.add_cog(MainCog(bot))