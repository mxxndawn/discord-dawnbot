import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')

    @commands.command(name="핑")
    async def ping2(self, ctx):
        embed = discord.Embed(title="ppii", description="iipp")
        await ctx.reply("퐁", embed=embed)
    
async def setup(bot):
    await bot.add_cog(Ping(bot))