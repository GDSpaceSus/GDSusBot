import requests, json

def user_data(user):
    user = user.lower().replace(' ', '%20')
    response = requests.get(f'https://gdbrowser.com/api/profile/{user}')
    if response.status_code == 200:
        response = response.json()
        try:
            data = response
            Username = f"Username: {data.get('username')}"
            Rank = f"Global rank: {data.get('rank')}"
            Stars = f"Stars: {data.get('stars')}"
            Moons = f"Moons: {data.get('moons')}"
            Diamonds = f"Diamonds: {data.get('diamonds')}"
            Coins = f"Coins: {data.get('coins')}"
            U_coins = f"User coins: {data.get('userCoins')}"
            Demons = f"Demons: {data.get('demons')}"
            Cp = f"CP: {data.get('cp')}"
            P_ID = f"Player ID: {data.get('playerID')}"
            A_ID = f"Account ID: {data.get('accountID')}"
            data_1 = f'{Username}\n{Rank}\n{Stars}\n{Moons}\n{Diamonds}\n{Coins}\n{U_coins}\n{Demons}\n{Cp}\n{P_ID}\n{A_ID}'
        except:
            data_1 = None
        try:
            data = response['classicDemonsCompleted']
            Easy = f"Easy: {data.get('easy')}"
            Medium = f"Medium: {data.get('medium')}"
            Hard = f"Hard: {data.get('hard')}"
            Insane = f"Insane: {data.get('insane')}"
            Extreme = f"Extreme: {data.get('extreme')}"
            Weekly = f"Weekly: {data.get('weekly')}"
            Gauntlet = f"Gauntlet: {data.get('gauntlet')}"
            data_2 = f'{Easy}\n{Medium}\n{Hard}\n{Insane}\n{Extreme}\n{Weekly}\n{Gauntlet}'
        except:
            data_2 = None
        try:
            data = response['platformerDemonsCompleted']
            Easy = f"Easy: {data.get('easy')}"
            Medium = f"Medium: {data.get('medium')}"
            Hard = f"Hard: {data.get('hard')}"
            Insane = f"Insane: {data.get('insane')}"
            Extreme = f"Extreme: {data.get('extreme')}"
            data_3 = f'{Easy}\n{Medium}\n{Hard}\n{Insane}\n{Extreme}'
        except:
            data_3 = None
        try:
            data = response['classicLevelsCompleted']
            Auto = f"Auto: {data.get('auto')}"
            Easy = f"Easy: {data.get('easy')}"
            Normal = f"Normal: {data.get('normal')}"
            Hard = f"Hard: {data.get('hard')}"
            Harder = f"Harder: {data.get('harder')}"
            Insane = f"Insane: {data.get('insane')}"
            Daily = f"Daily: {data.get('daily')}"
            Gauntlet = f"Gauntlet: {data.get('gauntlet')}"
            data_4 = f'{Auto}\n{Easy}\n{Normal}\n{Hard}\n{Harder}\n{Insane}\n{Daily}\n{Gauntlet}'
        except:
            data_4 = None
        try:
            data = response['platformerLevelsCompleted']
            Auto = f"Auto: {data.get('auto')}"
            Easy = f"Easy: {data.get('easy')}"
            Normal = f"Normal: {data.get('normal')}"
            Hard = f"Hard: {data.get('hard')}"
            Harder = f"Harder: {data.get('harder')}"
            Insane = f"Insane: {data.get('insane')}"
            Daily = f"Daily: {data.get('daily')}"
            data_5 = f'{Auto}\n{Easy}\n{Normal}\n{Hard}\n{Harder}\n{Insane}\n{Daily}'
        except:
            data_5 = None
        try:
            data = response
            Friend_requests = f"Friend requests: {data.get('friendRequests')}"
            Messages = f"Messages: {data.get('messages')}"
            Comment_history = f"Comment history: {data.get('commentHistory')}"
            Moderator = f"Moderator: {data.get('moderator')}"
            Youtube = f"Youtube: {data.get('youtube')}"
            Twitter = f"Twitter: {data.get('twitter')}"
            Twitch = f"Twitch: {data.get('twitch')}"
            data_6 = f'{Friend_requests}\n{Messages}\n{Comment_history}\n{Moderator}\n{Youtube}\n{Twitter}\n{Twitch}'
        except:
            data_6 = None
        message = (
            f'```User_data\n{data_1}\n```\n'
            f'```Other\n{data_6}\n```\n'
            f'```Levels\n{data_4}\n``` \n'
            f'```Demons\n{data_2}\n``` \n'
            f'```Platformers\n{data_5}\n``` \n'
            f'```Platformer_demons\n{data_3}\n```'
        )
        return message

def getUserComments(user, page):
    user = user.lower().replace(' ', '%20')
    message = ''
    playerID = getUserIDs(user).get('playerID')
    response = requests.get(f'https://gdbrowser.com/api/comments/{playerID}?type=commentHistory&page={page}&count=5').json()
    for data in response:
        base = (
            f"```LevelID:{data.get('levelID')}\n"
            f"Time: {data.get('date')}\n"
            f"Likes: {data.get('likes')}\n"
            f"Percent: {data.get('percent')}\n"
            f"Text: {data.get('content')}\n```\n"
        )
        message += base
    return message

def getUserPosts(user, page):
    user = user.lower().replace(' ', '%20')
    message = ''
    accountID = getUserIDs(user).get('accountID')
    response = requests.get(f'https://gdbrowser.com/api/comments/{accountID}?type=profile&page={page}&count=5').json()
    for data in response:
        base = (
            f"```\nTime: {data.get('date')}\n"
            f"Likes: {data.get('likes')}\n"
            f"Text: {data.get('content')}\n```\n"
        )
        message += base
    base = (
        f"```Other\n"
        f"Pages: {response[0].get('pages')}\n"
        f"Results: {response[0].get('results')}\n```\n"
    )
    message += base
    return message

def getUserIcon(user, num):
    user = user.lower().replace(' ', '%20')
    response = requests.get(f'https://gdbrowser.com/api/profile/{user}').json()
    if 1 <= num <= 8:
        if num == 1:
            n = 'ship'
        elif num == 2:
            n = 'ball'
        elif num == 3:
            n = 'ufo'
        elif num == 4:
            n = 'wave'
        elif num == 5:
            n = 'robot'
        elif num == 6:
            n = 'spider'
        elif num == 7:
            n = 'swing'
        elif num == 8:
            n = 'jetpack'
        return f'https://gdbrowser.com/icon/icon?form={n}&icon={response[n]}'
    elif num == 9:
        return f'https://gdbrowser.com/icon/icon?form=cube&icon={response["icon"]}'

def getUserIDs(user):
    data = { 'secret': 'Wmfd2893gb7', 'str': user }
    headers = { 'User-Agent': '' }
    data = requests.post('https://www.boomlings.com/database/getGJUsers20.php', data=data, headers=headers).text

    parts = data.split(':')
    user_dict = dict(zip(parts[0::2], parts[1::2]))

    strict_data = {
        'playerID': int(user_dict.get('2')),
        'accountID': int(user_dict.get('16')),
    }

    return strict_data