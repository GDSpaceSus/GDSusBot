def parseLevel(data):
    Name = f"Name: {data.get('name')}"
    Id = f"Level ID: {data.get('id')}"
    Author = f"Author: {data.get('author')}"
    Difficulty = f"Difficulty: {data.get('difficulty')}"
    Downloads = f"Downloads: {data.get('downloads')}"
    Coins = f"Coins: {data.get('coins')}"
    Likes = f"Likes: {data.get('likes')}"
    Length = f"Length: {data.get('length')}"
    Stars = f"Stars: {data.get('stars')}"
    Orbs = f"Orbs: {data.get('orbs', None)}"
    Diamonds = f"Diamonds: {data.get('diamonds')}"
    Cp = f"CP: {data.get('cp')}"
    Description = data.get('description')
    Featured = f"Featured: {data.get('featured')}"
    Epic = f"Epic: {data.get('epic')}"
    Legendary = f"Legendary: {data.get('legendary')}"
    Mythic = f"Mythic: {data.get('mythic')}"
    GameVersion = f"Game version: {data.get('gameVersion')}"
    Version = f"Version: {data.get('version')}"
    CopiedID = f"Copied ID: {data.get('copiedID')}"
    TwoPlayer = f"Two player: {data.get('twoPlayer')}"
    EditorTime = f"Editor time: {data.get('editorTime')}"
    TotalEditorTime = f"Total editor time: {data.get('totalEditorTime')}"
    VerifiedCoins = f"Verified Coins: {data.get('verifiedCoins')}"
    StarsRequested = f"Stars requested: {data.get('starsRequested')}"
    Ldm = f"LDM: {data.get('ldm')}"
    Objects = f"Objects: {data.get('objects')}"
    SongName = f"Song name: {data.get('songName')}"
    SongAuthor = f"Song author: {data.get('songAuthor')}"
    SongSize = f"Song size: {data.get('songSize')}"
    SongID = f"Song ID: {data.get('songID')}"
    data_1 = f'{Name}\n{Author}\n{Id}\n{Downloads}\n{Likes}\n{Stars}\n{Coins}\n{Orbs}\n{Diamonds}\n{Cp}\n{Difficulty}\n{Length}'
    data_2 = Description
    data_3 = f'{Objects}\n{StarsRequested}\n{GameVersion}\n{Version}\n{CopiedID}\n{EditorTime}\n{TotalEditorTime}\n{Featured}\n{Epic}\n{Legendary}\n{Mythic}\n{TwoPlayer}\n{Ldm}\n{VerifiedCoins}'
    data_4 = f"{SongName}\n{SongAuthor}\n{SongSize}\n{SongID}"
    message = (
        f'```Level\n{data_1}\n```\n'
        f'```Description\n{data_2}\n```\n'
        f'```Settings\n{data_3}\n``` \n'
        f'```Song\n{data_4}\n```'
    )
    return message