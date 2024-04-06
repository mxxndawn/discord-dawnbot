from discord import Interaction
from discord.ext.commands import Bot, Cog
from discord.app_commands.commands import Group, describe, command

class UtileCog(Cog):
    util_group = Group(name='util', description='유틸리티 커멘드 그룹')

    @util_group.command()
    async def add(self, ctx: Interaction, num1: int, num2: int):
        await ctx.response.send_message(f'{num1} + {num2} = {num1+num2}')

async def setup(bot: Bot):
    await bot.add_cog(UtileCog())