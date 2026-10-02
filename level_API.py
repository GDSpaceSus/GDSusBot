import requests
from level_text import parseLevel

def getLevelData(levelID):
    response = requests.get(f'https://gdbrowser.com/api/search/{levelID}')
    if response.status_code == 200: return [parseLevel(response.json()[0]), response.json()[0].get('author')]
    else: return 'Уровень не найден!'

def dailyWeeklyEventLevelData(param):
    if param == 'weekly': response = requests.get('https://gdbrowser.com/api/level/weekly')
    elif param == 'event': response = requests.get('https://gdbrowser.com/api/level/event')
    else: response = requests.get('https://gdbrowser.com/api/level/daily')
    data = parseLevel(response.json())
    return data

def getUserLevelsData(user, page):
    user = user.lower().replace(' ', '%20')
    message = ''
    data = requests.get(f"https://gdbrowser.com/api/search/{user}?user&page={page}count=5").json()
    for level in data:
        base = (
            f"```Level\nName: {level.get('name')}\n"
            f"Level ID: {level.get('id')}\n```\n"
        )
        message += base
    return message

def getLevelComments(levelID, page):
    try:
        message = ''
        response = requests.get(f'https://gdbrowser.com/api/comments/{levelID}?page={page}&count=5').json()
        for data in response:
            base = (
                f"```\nUsername: {data.get('username')}\n"
                f"Time: {data.get('date')}\n"
                f"Likes: {data.get('likes')}\n"
                f"Text: {data.get('content')}\n"
                f"Percent: {data.get('percent')}\n```\n"
            )
            message += base
        base = (
            f"```Other\n"
            f"Pages: {response[0].get('pages')}\n"
            f"Results: {response[0].get('results')}\n```\n"
        )
        message += base
        return message
    except:
        return 'Ошибка...'

def getSearchLevelsData(level, page):
    message = ''
    ids = []
    users = []
    response = requests.get(f'https://gdbrowser.com/api/search/{level}?level&page={page}&count=5').json()
    for data in response:
        ids.append(data.get('id'))
        users.append(data.get('author'))
        base = (
            f"```\nName: {data.get('name')}\n"
            f"Level ID: {data.get('id')}\n"
            f"Author: {data.get('author')}\n"
            f"Likes: {data.get('likes')}\n"
            f"Downloads: {data.get('downloads')}\n```\n"
        )
        message += base
    return [message, [ids, users]]