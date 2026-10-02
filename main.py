import asyncio, requests, random, time, fandom, uuid

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, URLInputFile, CallbackQuery
from aiogram.enums import ParseMode

from user_API import *
from level_API import *
from config import *
from keyboard import *

def restart_ids():
    global ids
    ids = read_list_from_file()

def setData(data):
    key = uuid.uuid4().hex[:8]
    database[key] = data
    return key

def getData(key):
    return database.pop(key)

TOKEN = ''
bot = Bot(token=TOKEN)
dp = Dispatcher()

ids = read_list_from_file()
database = {}

fandom.set_lang('ru')
fandom.set_wiki('geometry-dash')

@dp.message(CommandStart())
async def cmd_start(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        await message.reply('Приветик! Чем могу помочь?')

@dp.message(Command('cmd'))
async def send_debug(message: Message):
    if int(message.from_user.id) == 7927547731:
        chatID = int(message.chat.id)
        data = message.text.replace('/cmd', '').lower().strip()
        my_list = read_list_from_file()

        try:
            if data == '':
                if chatID not in my_list:
                    my_list.append(chatID)
                    write_list_to_file(my_list)
                    restart_ids()

            elif 'l' in data:
                await message.reply(str(my_list))

            elif 'r' in data.split():
                mess = data.replace('r ', '')
                my_list.pop(int(mess))
                write_list_to_file(my_list)
                restart_ids()

            elif 'd' in data:
                if chatID in my_list:
                    my_list.pop(my_list.index(chatID))
                    write_list_to_file(my_list)
                    restart_ids()

            elif data.replace('-', '').isdigit():
                if int(data) not in my_list:
                    my_list.append(int(data))
                    write_list_to_file(my_list)

        except:
            await message.reply('Ошибка...')

@dp.message(Command('help'))
async def cmd_help(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        await message.reply('https://t.me/GDSusBotHelp')

@dp.message(Command('ping'))
async def cmd_help(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        await message.reply('Я живой :3')

@dp.message(Command('daily'))
async def cmd_daily(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        try:
            data = dailyWeeklyEventLevelData('daily')
            await message.reply(data, parse_mode=ParseMode.MARKDOWN)
        except:
            await message.reply('Ошибка...')

@dp.message(Command('weekly'))
async def cmd_weekly(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        try:
            data = dailyWeeklyEventLevelData('weekly')
            await message.reply(data, parse_mode=ParseMode.MARKDOWN)
        except:
            await message.reply('Ошибка...')

@dp.message(Command('event'))
async def cmd_event(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        try:
            data = dailyWeeklyEventLevelData('event')
            await message.reply(data, parse_mode=ParseMode.MARKDOWN)
        except:
            await message.reply('Ошибка...')

@dp.message(Command('getLevelComments'))
async def cmd_comments(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        try:
            data = cmdsplit(message.text.replace('/getLevelComments', ''))

            levelID = data[0]
            page = int(data[1])

            data = getLevelComments(levelID, page)
            await message.reply(data, parse_mode=ParseMode.MARKDOWN)
        except:
            await message.reply('Ошибка...')

@dp.message(Command('getUserComments'))
async def cmd_user_comments(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        try:
            data = cmdsplit(message.text.replace('/getUserComments', ''))

            user = data[0]
            page = int(data[1])

            data = getUserComments(user, page)
            await message.reply(data, parse_mode=ParseMode.MARKDOWN)
        except:
            await message.reply('Ошибка...')

@dp.message(Command('getUserPosts'))
async def cmd_user_posts(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        try:
            data = cmdsplit(message.text.replace('/getUserPosts', ''))

            user = data[0]
            page = int(data[1])

            data = getUserPosts(user, page)
            await message.reply(data, parse_mode=ParseMode.MARKDOWN)
        except Exception as e:
            print(e)
            await message.reply('Ошибка...')

@dp.message(Command('searchLevel'))
async def cmd_search(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        try:
            data = cmdsplit(message.text.replace('/searchLevel', ''))

            level = data[0]
            page = int(data[1])

            data = getSearchLevelsData(level, page)

            key1 = setData(data[1])
            key2 = setData([page, level])

            await message.reply(data[0], parse_mode=ParseMode.MARKDOWN, reply_markup=getLevelsKeyboard(key1, key2, page))
        except Exception as e:
            print(e)
            await message.reply('Ошибка...')

@dp.message(Command('getLevelInfo'))
async def cmd_level(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        try:
            levelID = message.text.replace('/getLevelInfo', '').strip()
            data = getLevelData(levelID)

            key1 = setData(levelID)
            key2 = setData(data[1])

            if requests.get(f'https://levelthumbs.prevter.me/thumbnail/{levelID}/high').status_code == 200:
                await message.reply(f'[\u200b](https://levelthumbs.prevter.me/thumbnail/{levelID}/high)' + data[0], parse_mode=ParseMode.MARKDOWN, reply_markup=getLevelKeyboard(key1, key2))
            else:
                await message.reply(data[0], parse_mode=ParseMode.MARKDOWN, reply_markup=getLevelKeyboard(key2, key1))
        except:
            await message.reply('Ошибка...')

@dp.message(Command('getUserLevels'))
async def cmd_user_levels(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        try:
            data = cmdsplit(message.text.replace('/getUserLevels', ''))
            
            user = data[0]
            page = int(data[1])
            
            data = getUserLevelsData(user, page)
            await message.reply(data, parse_mode=ParseMode.MARKDOWN)
        except:
            await message.reply('Ошибка...')

@dp.message(Command('getUserInfo'))
async def cmd_user(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        try:
            user = message.text.replace('/getUserInfo', '').strip()
            data = user_data(user)
            await message.reply(data, parse_mode=ParseMode.MARKDOWN)
        except:
            await message.reply('Ошибка...')

@dp.message(Command('getUserIcon'))
async def cmd_user_icon(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        try:
            data = cmdsplit(message.text.replace('/getUserIcon', ''))

            user = data[0]
            num = int(data[1])

            url = getUserIcon(user, num)
            image = URLInputFile(url)
            await message.reply_photo(image)
        except:
            await message.reply('Ошибка...')

@dp.message(Command('cat'))
async def send_cat_image(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        try:
            t = str(time.time())
            randomMeow = random.choice(['Мяу', 'Мур', 'Мя', 'Ня', 'Мяф', 'Мрр'])
            mess = message.text.replace('/cat', '').strip()
            if mess == '': mess = random.choice(['1', '2', '3'])
            if mess == '1':
                response = requests.get(f"https://api.thecatapi.com/v1/images/search?v={t}")
                cat_photo = response.json()[0]['url']
                await message.reply_photo(cat_photo, caption=randomMeow)
            elif mess == '2':
                cat_photo = f'https://cataas.com/cat?v={t}'
                await message.reply_photo(cat_photo, caption=randomMeow)
            elif mess == '3':
                cat_gif = f'https://cataas.com/cat/gif?v={t}'
                await message.reply_animation(cat_gif, caption=randomMeow)
            else:
                mess = cmdsplit(mess)
                text = mess[0].replace(' ', '%20')
                if len(mess) == 1:
                    cat_photo = f'https://cataas.com/cat/says/{text}?v={t}'
                    await message.reply_photo(cat_photo, caption=randomMeow)
                elif len(mess) == 2:
                    cat_photo = f'https://cataas.com/cat/says/{text}?&fontSize={mess[1]}&v={t}'
                    await message.reply_photo(cat_photo, caption=randomMeow)
        except:
            await message.reply("Ошибка... XwX")

@dp.message(Command('gif'))
async def send_mess_image(message: Message):
    chatID = int(message.chat.id)
    if chatID in ids:
        try:
            data = message.text.replace('/gif ', '')
            response = requests.get(f'')
            await message.reply_animation(response.json()['data']['data'][0]['file']['hd']['gif']['url'])
        except:
            await message.reply('Ошибка...')


@dp.callback_query(lambda x: "sl_" in x.data)
async def info_more(callback: CallbackQuery):
    if "sl_<" in callback.data:
        data = getData(callback.data.split('_')[2])

        level = data[1]
        page = data[0] - 1

        data = getSearchLevelsData(level, page)

        key1 = setData(data[1])
        key2 = setData([page, level])

        await callback.message.edit_text(text=data[0], parse_mode=ParseMode.MARKDOWN, reply_markup=getLevelsKeyboard(key1, key2, page))
        await callback.answer()

    elif "sl_>" in callback.data:
        data = getData(callback.data.split('_')[2])

        level = data[1]
        page = data[0] + 1

        data = getSearchLevelsData(level, page)

        key1 = setData(data[1])
        key2 = setData([page, level])

        await callback.message.edit_text(text=data[0], parse_mode=ParseMode.MARKDOWN, reply_markup=getLevelsKeyboard(key1, key2, page))
        await callback.answer()

    else:
        data = getData(callback.data.split('_')[2])

        num = int(callback.data.split('_')[1])
        levelID = data[0][num - 1]

        data = getLevelData(levelID)

        key1 = setData(levelID)
        key2 = setData(data[1])

        url = ''
        if requests.get(f'https://levelthumbs.prevter.me/thumbnail/{levelID}/high').status_code == 200:
            url = f'[\u200b](https://levelthumbs.prevter.me/thumbnail/{levelID}/high)'

        await callback.message.edit_text(text=url + data[0], parse_mode=ParseMode.MARKDOWN, reply_markup=getLevelKeyboard(key1, key2))
        await callback.answer()


@dp.callback_query(lambda x: "ld_" in x.data)
async def info_more2( callback: CallbackQuery):
    if 'ld_a' in callback.data:
        user = getData(callback.data.split('_')[2])

        await callback.message.edit_text(text=user_data(user), parse_mode=ParseMode.MARKDOWN)
        await callback.answer()

    elif 'ld_c' in callback.data:
        levelID = getData(callback.data.split('_')[2])

        await callback.message.edit_text(text=getLevelComments(levelID, 0), parse_mode=ParseMode.MARKDOWN)
        await callback.answer()


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
