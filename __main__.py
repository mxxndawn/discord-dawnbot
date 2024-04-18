from os import listdir
from asyncio import run
from discord import Intents, Interaction
from discord.ext.commands import Bot, when_mentioned
from const import get_info

#var
intents = Intents()
intents.messages = True
intents.message_content = True
bot = Bot(when_mentioned, intents= intents)

@bot.event # 실행 알람 및 명령어 호출
async def on_ready():
    print(f'Start in as {bot.user}')
    await bot.tree.sync()

'''
@bot.tree.command(name='리로드')
async def reload_cog(ctx: Interaction, cog_name=None):
    if cog_name is None:
        cogs = [filename[:-3] for filename in listdir('Cogs') if filename.endswith('.py')]
        await ctx.response.send_message("사용 가능한 코그:\n" + "\n".join(cogs))
    else:
        try:
            bot.reload_extension(f"Cogs.{cog_name}")
            await ctx.response.send_message(f"{cog_name} : 성공적으로 리로드 되었습니다!")
        except Exception as e:
            await ctx.response.send_message(f"{cog_name} : 리로드에 실패했습니다. : {e}")
'''

async def load_extensions(): #코그 파일 순환 로드
    for filename in listdir('Cogs'):
        if not filename.endswith('.py'):
            continue
        cog_name = f'Cogs.{filename[:-3]}'
        await bot.load_extension(cog_name)
        print(f'Cog Load: {cog_name}')

def main(): #명령어 Cogs 실행, 디스코드 봇 실행
    run(load_extensions())
    bot.run(get_info('bot_info','bot_token'))

if __name__ == '__main__':
    main()