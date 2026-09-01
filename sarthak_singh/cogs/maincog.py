from discord.ext import commands
from discord import app_commands
import discord
import asyncio
import random

gameData = {}

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="start")
    async def start(self, ctx, gangster_name: str = None, gang_name: str = None):
        if gangster_name == None or gang_name == None:
            return await ctx.send("Use proper syntax: `!start <gangster name> <gang name>`")
        gameData[ctx.author.id] = {"gang": gang_name, "cash" : 10000, "muscle": 1}
        print(gameData)
        await ctx.send(f"Don {gangster_name} sends his regards from {gang_name}.")

    @commands.command(name="mug")
    async def mug(self, ctx):
        if ctx.author.id not in gameData:
            return await ctx.send("You do not have a gang yet, try !start")
        msg = await ctx.reply("Wait for the target to look away...")
        await asyncio.sleep(random.randint(2,6))
        await msg.edit(content="🚨 GO! REACT NOW!")
        await msg.add_reaction("👛")

        def check(reaction, user):
            return user == ctx.author and reaction.message.id == msg.id and str(reaction.emoji) == "👛"
        
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=2.0, check=check)
        except asyncio.TimeoutError:
            penalty = random.randint(6,10)*100
            gameData[ctx.author.id]["cash"] -= penalty
            await ctx.send(f"You weren't fast enough, you got caught and had to pay {penalty} as penalty")
        else:
            earned = random.randint(2,5)*100
            gameData[ctx.author.id]["cash"] += earned
            await ctx.send(f"You successfully stole {earned}")


    @commands.command(name="cash")
    async def cash(self, ctx):
        if ctx.author.id not in gameData:
            return await ctx.send("You do not have a gang yet, try !start")

        await ctx.send(f"Your current balance is {gameData[ctx.author.id]["cash"]}")

    @commands.command(name="extort")
    async def extort(self, ctx):
        if random.randint(1,3) == 1:
            pay = random.randint(1,4)*100
            gameData[ctx.author.id]["cash"] += pay
            await ctx.send(f"The shopkeeper agreed to pay {pay} as protection money")
        else:
            await ctx.send("The shopkeeper refused to pay protection money, maybe get more manpower?")



async def setup(bot):
    await bot.add_cog(MainCog(bot))