from asyncio import sleep # 임시 임포트
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
    
    @ex_group.command(description='embed 테스트')
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

async def setup(bot: Bot):
    await bot.add_cog(ExCog())