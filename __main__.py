from os import listdir
from asyncio import run
from discord import Intents, Interaction, Embed
from discord.ext.commands import Bot, when_mentioned
from const import get_info

#var
intents = Intents()
intents.messages = True
intents.message_content = True
bot = Bot(when_mentioned, intents= intents)

@bot.event #명령어 호출
async def on_ready():
    await bot.tree.sync()

async def load_extensions(): #코그 파일 순환 로드
    for filename in listdir('Cogs'):
        if not filename.endswith('.py'):
            continue
        cog_name = f'Cogs.{filename[:-3]}'
        await bot.load_extension(cog_name)
        print(f'Cog Load: {cog_name}')

def main(): #명령어 Cogs 실행, 디스코드 봇 실행
    run(load_extensions())
    bot.run(get_info('discord_bot_token'))

if __name__ == '__main__':
    main()