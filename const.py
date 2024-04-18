from json import load

def load_json():
    with open('bot_info.json', 'r') as file:
        return load(file)

def get_info(section: str, *keys: str):
    data = load_json()
    section_data = data.get(section)
    for key in keys:
        result = section_data.get(key)
    return result


"""
print(get_info("aws_info","AWS_ACCESS_KEY_ID"))
print(get_info("aws_info","AWS_SECRET_ACCESS_KEY"))
print(get_info("aws_info","REGION_NAME"))

from json import load

with open('discord_bot_info.json', 'r') as file:
    info = load(file)

def _get(json: dict, path: str):
    path = path.split('.')
    while path:
        json = json.get(path.pop(0))
        if json is None:
            return
        return json
    
def get_discord_info(path):
    return _get(info, path)
"""