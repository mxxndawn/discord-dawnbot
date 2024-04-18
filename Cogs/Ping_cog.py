from discord import Interaction
from discord.ext.commands import Bot, Cog
from discord.app_commands.commands import Group, describe, command

class PingCog(Cog):
    ping_group = Group(name='테스트용', description='유틸리티 커멘드 그룹')

    @command(description='pong이라고 대답합니다.') #명령어 : 핑
    async def ping(self, ctx: Interaction):
        await ctx.response.send_message('Pong')

    @command(description='입력한 메세지를 반환합니다.')
    @describe(message='반환할 메세지')
    async def echo(self, ctx: Interaction, message: str):
        await ctx.response.send_message(message)

async def setup(bot: Bot):
    await bot.add_cog(PingCog())