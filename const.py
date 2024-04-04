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
    
def get_info(path):
    return _get(info, path)