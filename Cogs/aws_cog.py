from json import load
from discord import Interaction
from discord.ext.commands import Bot, Cog
from discord.app_commands.commands import Group
from const  import get_info
import boto3

temp_instance_info = {}

ec2 = boto3.client('ec2',
                   aws_access_key_id=get_info("aws_info","AWS_ACCESS_KEY_ID"),
                   aws_secret_access_key=get_info("aws_info","AWS_SECRET_ACCESS_KEY"),
                   region_name=get_info("aws_info","REGION_NAME"))

# EC2 인스턴스를 시작하는 함수
def start_ec2_instance(instance_id):
    ec2.start_instances(InstanceIds=[instance_id])

# EC2 인스턴스를 중지하는 함수
def stop_ec2_instance(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])

# EC2 인스턴스 상태를 가져오는 함수
def get_ec2_instance_status(instance_id):
    response = ec2.describe_instances(InstanceIds=[instance_id])
    status = response['Reservations'][0]['Instances'][0]['State']['Name']
    return status

# EC2 인스턴스 목록을 가져오는 함수
def get_ec2_instance_list():
    response = ec2.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            # 인스턴스에 'Name' 태그가 있는지 확인하고 가져옵니다.
            name = None
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    name = tag['Value']
                    break
            # 만약 'Name' 태그가 없으면 인스턴스 ID를 이름으로 사용합니다.
            if not name:
                name = instance_id
            # 인스턴스 ID와 이름을 문자열로 변환하여 리스트에 저장합니다.
            instances.append(f"{instance_id}: {name}")
    return instances

class AwsCog(Cog):
    aws_group = Group(name='서버', description='AWS Server Commands Group')

    @aws_group.command(name='목록', description='게임서버의 전체 상태를 확인합니다')
    async def ec2_status(self, ctx: Interaction):
        instances = get_ec2_instance_list()
        if instances:
            instance_list_str = '\n'.join(instances)
            await ctx.response.send_message(f'Current running instances:\n{instance_list_str}')
        else:
            await ctx.response.send_message('No running instances found.')

    @aws_group.command(name='상태', description='게임서버의 상태를 확인합니다')
    async def ec2_status_one(self, ctx: Interaction, 서버이름: str): #리스트 불러오기
        pass
    @aws_group.command(name='실행', description='게임서버를 실행 합니다')
    async def ec2_start(self, ctx: Interaction, 서버이름: str): #리스트 불러오기
        pass
    @aws_group.command(name='종료', description='게임서버를 종료 합니다')
    async def ec2_stop(self, ctx: Interaction, 서버이름: str): #리스트 불러오기
        pass
    @aws_group.command(name='재시작', description='게임서버를 재시작 합니다')
    async def ec2_reboot(self, ctx: Interaction, 서버이름: str): #리스트 불러오기
        pass

async def setup(bot: Bot):
    await bot.add_cog(AwsCog())

'''
gpt로 생성한 내용.
인턴스 목록을 임시저장하고 리스트에서 인스턴스를 선택하여 실행할 수 있도록 하는거임.
자세한 내용과 추가질문은 chatgpt3 apple id로 로그인하여 할것
import discord
from discord.ext import commands

# 임시로 저장할 인스턴스 정보 딕셔너리
temp_instance_info = {}

# 봇 설정
bot = commands.Bot(command_prefix='!')

# EC2 인스턴스 목록을 가져오는 함수
def get_ec2_instance_list():
    response = ec2.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            name = None
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    name = tag['Value']
                    break
            if not name:
                name = instance_id
            # 인스턴스 ID와 이름을 딕셔너리에 저장
            temp_instance_info[instance_id] = name
            # 선택 가능한 리스트에 추가
            instances.append(f"{instance_id}: {name}")
    return instances

# 명령어: !인스턴스목록
@bot.command()
async def 인스턴스목록(ctx):
    instances = get_ec2_instance_list()
    # 선택 가능한 리스트를 보여줍니다.
    await ctx.send("인스턴스 목록:\n" + "\n".join(instances))

# 명령어: !인스턴스실행 <instance_id>
@bot.command()
async def 인스턴스실행(ctx, instance_id):
    if instance_id in temp_instance_info:
        name = temp_instance_info[instance_id]
        await ctx.send(f"인스턴스 '{name}'(ID: {instance_id})를 실행합니다.")
        # 인스턴스 실행하는 코드 작성
    else:
        await ctx.send("해당 인스턴스를 찾을 수 없습니다.")

# 봇 실행
bot.run("YOUR_BOT_TOKEN")

'''