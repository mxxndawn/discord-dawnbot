from asyncio import sleep # 임시 임포트
import typing
import discord
from discord import Interaction, Embed # embed 임포트
from discord.ext.commands import Bot, Cog
from discord.app_commands.commands import Group, describe, Command

class ExCog(Cog):
    ex_group = Group(name='ex', description='예제 커맨드 그룹')

    @ex_group.command(description='오래걸리는 명령어 예제')
    async def longtime_command(self, ctx: Interaction):
        await ctx.response.defer()
        await sleep(8) #이 부분에 오래걸리는 명령어 입력
        await ctx.edit_original_response(content='명령 실행완료')
    
    @ex_group.command(name='임베드', description='embed 테스트')
    async def embed(self, ctx: Interaction):
        embed = Embed(title='타이틀', description='설명', color=0x4287f5)
        embed.set_author(name=f'{ctx.user.name}', icon_url=f'{ctx.user.avatar}')
        embed.set_footer(text='footer is this', icon_url=f'{ctx.user.avatar}')
        embed.set_image(url=f'{ctx.user.avatar}')
        embed.set_thumbnail(url=f'{ctx.user.avatar}')
        embed.add_field(name='메시지 보낸 사람 id', value=f'{ctx.user.id}')
        embed.add_field(name='메시지 보낸 사람 닉네임', value=f'{ctx.user.name}')
        embed.add_field(name='메시지 보낸 사람 프로필사진', value=f'{ctx.user.avatar}')
        await ctx.response.send_message(embed=embed)

    @ex_group.command()
    async def channel_set(self, ctx: Interaction, 채널: typing.Union[discord.TextChannel]):# str이 아니라 채널목록 표시하게 할 것
        embed = Embed(title='ss', description='eee')
        await ctx.send(embed=embed)
        #당장은 에러. 채널을 고르면 해당 채널로 지정하여 메세지를 보내는 기능을 만들것.
        #메세지를 보낸후에는 별도로 기록하여 어떤서버에서 어떤 채널을 지정했는지 기록.
        #만약 서버에서 채널지정을 요청하는경우 기존 지정된 채널이 있다면 오류메세지 보내기.
        #지정된 채널이 없다면 지정채널을 저장한후 1번으로.

async def setup(bot: Bot):
    await bot.add_cog(ExCog())