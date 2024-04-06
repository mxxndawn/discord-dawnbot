from discord import Interaction
from discord.ext.commands import Bot, Cog
from discord.app_commands.commands import Group

class AwsCog(Cog):
    aws_group = Group(name='서버', description='AWS Server Commands Group')

    @aws_group.command(name='전체상태', description='게임서버의 전체 상태를 확인합니다')
    async def aws_status_all(self, ctx: Interaction):
        pass
    @aws_group.command(name='상태', description='게임서버의 상태를 확인합니다')
    async def aws_status_one(self, ctx: Interaction, 서버: str): #리스트 불러오기
        pass
    @aws_group.command(name='실행', description='게임서버를 실행 합니다')
    async def aws_server_start(self, ctx: Interaction, 서버목록: str): #리스트 불러오기
        pass
    @aws_group.command(name='종료', description='게임서버를 종료 합니다')
    async def aws_server_stop(self, ctx: Interaction, 서버목록: str): #리스트 불러오기
        pass
    @aws_group.command(name='재시작', description='게임서버를 재시작 합니다')
    async def aws_server_reboot(self, ctx: Interaction, 서버목록: str): #리스트 불러오기
        pass

async def setup(bot: Bot):
    await bot.add_cog(AwsCog())