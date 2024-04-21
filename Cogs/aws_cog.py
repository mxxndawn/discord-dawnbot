import json
import discord
from discord import Interaction, Embed, Button
from discord.ui import Select, View
from discord.ext.commands import Bot, Cog
from discord.app_commands.commands import Group
from const  import get_info
import boto3

access_key_id = get_info("aws_info","AWS_ACCESS_KEY_ID")
secret_access_key = get_info("aws_info","AWS_SECRET_ACCESS_KEY")
region_name = get_info("aws_info","REGION_NAME")

class EC2Manager:
    def __init__(self, access_key_id, secret_access_key, region_name):
        self.ec2 = boto3.client('ec2',
                                aws_access_key_id=access_key_id,
                                aws_secret_access_key=secret_access_key,
                                region_name=region_name)
        
        with open('instance_specs.json', 'r') as f:
            self.instance_specs = json.load(f)

    def start_instances(self, instance_ids):
        response = self.ec2.start_instances(InstanceIds=instance_ids)
        return response

    def stop_instances(self, instance_ids):
        response = self.ec2.stop_instances(InstanceIds=instance_ids)
        return response

    def reboot_instances(self, instance_ids):
        response = self.ec2.reboot_instances(InstanceIds=instance_ids)
        return response
    
    def get_instance_info(self):
        instance_info = {}
        response = self.ec2.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_name = ""
                instance_ram = ""
                instance_cpu = ""
                launch_time = ""

                # 인스턴스 이름이 태그에 Name이라는 키로 저장되어 있다고 가정
                for tag in instance.get('Tags', []):
                    if tag['Key'] == 'Name':
                        instance_name = tag['Value']

                # 인스턴스 유형 가져오기
                instance_type = instance.get('InstanceType', '')

                # 인스턴스 스펙 가져오기
                instance_ram, instance_cpu = self.get_instance_specs(instance_type)

                # 인스턴스 생성일 가져오기
                launch_time = instance['LaunchTime'].strftime("%Y-%m-%d %H:%M:%S")

                instance_info[instance_name] = {
                    'instance_id': instance_id,
                    'instance_type': instance_type,
                    'instance_ram': instance_ram,
                    'instance_cpu': instance_cpu,
                    'launch_time': launch_time
                }

        return instance_info

    def get_instance_specs(self, instance_type):
        # 인스턴스 유형에 따른 스펙 가져오기
        if instance_type in self.instance_specs:
            instance_ram = self.instance_specs[instance_type]['ram']
            instance_cpu = self.instance_specs[instance_type]['cpu']
        else:
            instance_ram = 'Unknown'
            instance_cpu = 'Unknown'
        
        return instance_ram, instance_cpu

ec2_manager = EC2Manager(access_key_id, secret_access_key, region_name)

class AwsCog(Cog):
    aws_group = Group(name='서버', description='AWS Server Commands Group')

    @aws_group.command(name='test')
    async def ec2_test(self, ctx: Interaction):
        instance_info = ec2_manager.get_instance_info()
        embed = Embed(title="EC2 Instance Info", color=0x4287f5)
        for instance_name, info in instance_info.items():
            embed.add_field(name=instance_name, value=f"ID: {info['instance_id']}\nType: {info['instance_type']}\nRAM: {info['instance_ram']}\nCPU: {info['instance_cpu']}\nLaunch Time: {info['launch_time']}", inline=False)
        await ctx.response.send_message(embed=embed)


    @aws_group.command(name='관리', description='게임서버 관리창을 호출합니다')
    async def ec2_manager(self, ctx: Interaction): #리스트 불러오기
        select = Select(
            placeholder="관리하실 서버를 선택해 주세요!", 
            options=[
                discord.SelectOption(
                    label="Cloudy", 
                    description='Cloudy weather'),
                discord.SelectOption(
                    label="Rainy", 
                    description="It's Raining")
            ])
        
        async def server_callback(interaction):
            embed = Embed(title=f"{select.values[0]}", description='설명', color=0x4287f5)
            embed.set_author(name=f'{ctx.user.name}', icon_url=f'{ctx.user.avatar}')
            embed.set_footer(text='footer is this', icon_url=f'{ctx.user.avatar}')
            embed.set_image(url=f'{ctx.user.avatar}')
            embed.set_thumbnail(url=f'{ctx.user.avatar}')
            embed.add_field(name='메시지 보낸 사람 id', value=f'{ctx.user.id}')
            embed.add_field(name='메시지 보낸 사람 닉네임', value=f'{ctx.user.name}')
            embed.add_field(name='메시지 보낸 사람 프로필사진', value=f'{ctx.user.avatar}')
            button = Button()
            await interaction.response.send_message(embed=embed)
            await interaction.respanse.send_message(button=button)
            # await interaction.response.send_message(f"you chose: {select.values[0]}")

        select.callback = server_callback
        view = View()
        view.add_item(select)

        await ctx.response.send_message("1", view=view)
        # ec2 인스턴스 리스트를 불러옴
        # 드롭다운 메뉴로 인스턴스 목록을 보여줌
        # 사용자 입력 -> 드롭다운에서 인스턴스를 선택
        # 드롭다운 메세지 삭제후 새로운 메세지로 embed 및 button ui 출력
        # embed : 서버이름, 게임 이미지, 생성날짜, 업타임,
        # button : 시작, 종료, 재시작

async def setup(bot: Bot):
    await bot.add_cog(AwsCog())

'''

    @aws_group.command(name='목록', description='게임서버의 전체 상태를 확인합니다')
    async def ec2_status(self, ctx: Interaction):
        pass

    @aws_group.command(name='상태', description='게임서버의 상태를 확인합니다')
    async def ec2_status_one(self, ctx: Interaction, 서버이름: str): #리스트 불러오기
        pass

    @aws_group.command(name='종료', description='게임서버를 종료 합니다')
    async def ec2_stop(self, ctx: Interaction, 서버이름: str): #리스트 불러오기
        pass

    @aws_group.command(name='재시작', description='게임서버를 재시작 합니다')
    async def ec2_reboot(self, ctx: Interaction, 서버이름: str): #리스트 불러오기
        pass

'''