from discord import Interaction
from discord.ext.commands import Bot, Cog
from discord.app_commands.commands import Group, describe, command

class UtileCog(Cog):
    util_group = Group(name='util', description='유틸리티 커멘드 그룹')

    @command()
    async def add(self, ctx: Interaction, num1: int, num2: int):
        await ctx.response.send_message(f'{num1} + {num2} = {num1+num2}')

    @util_group.command(description='pong이라고 대답합니다.') #명령어 : 핑
    async def ping(self, ctx: Interaction):
        await ctx.response.send_message('Pong')

    @util_group.command(description='입력한 메세지를 반환합니다.')
    @describe(message='반환할 메세지')
    async def echo(self, ctx: Interaction, message: str):
        await ctx.response.send_message(message)

async def setup(bot: Bot):
    await bot.add_cog(UtileCog())