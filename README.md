# <center>비 전문가가 만드는 디코봇</center>

<center>
비 전문가가 유튜브, 스택오버플로우, ChatGPT를 뒤져가며<br>취미로 디소코드 봇을 만드는 프로젝트 입니다.<br>우선 AWS의 EC2 인스턴스를 조회하고 시작, 종료 하는 기능을 구현 할 예정입니다.<br>해당 기능을 구현한뒤에는 기능 개선과 더불어 필요한 추가 기능을 업데이트 할 예정입니다.
</center>

## 실행환경
디스코드 봇을 사용하기 위해선 하단의 표시된 파일이 최상위 폴더에 존재해야하며, 제시된 양식대로 내용이 채워져 있어야 합니다.<br><b>Not Required</b> : 필수가 아닙니다. 비워두어도 문제가 없습니다.<br><b>Required</b> : 필수입니다. 반드시 채워져야하는 부분입니다.

   1. bot_info.json
        ```json
        {
            "bot_info": {
                "application_id": "Not Required",
                "public_key": "Not Required",
                "bot_token": "Required"
            },
            "aws_info": {
                "AWS_ACCESS_KEY_ID": "Required",
                "AWS_SECRET_ACCESS_KEY": "Required",
                "REGION_NAME": "Required"
            }
        }
        ```
<br>디스코드 봇을 사용하기 위해선 하단에 제시된 모듈이 설치되어 있어야 합니다. <br>pipenv를 사용하여 개발한 환경과 동일한 환경에서 실핼할 수 있습니다.<br><b>Not Required</b> : 필수가 아닙니다. 비워두어도 문제가 없습니다.<br><b>Required</b> : 필수입니다. 반드시 채워져야하는 부분입니다.
1. pip install list
   1. discord.py
   2. boto3

## TO-DO
- [x] aws_add ec2 module
- [x] aws_boto3로 정보 가져오기
- [ ] aws_ec2 인스턴스 목록을 가져오기
- [ ] aws_ec2 인스턴스 목록을 embed로 가져오기
- [ ] aws_ec2 인스턴스 시작, 종료 기능 추가
- [ ] aws_ec2 인스턴스 시작, 종료 기능에 인스턴스를 선택할 수 있는 드로다운 기능 추가
- [ ] fn_지정채널(텍스트채널)설정 기능 구상
- [ ] fn_지정채널에 고정 메세지 전송(사라지지않음)
- [ ] fn_지정채널 메세지 반복 업데이트 기능 추가
- [ ] 