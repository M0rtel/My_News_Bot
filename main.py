import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from parsing_anime import get_data_anime
from parsing_new_film import get_data_film
from parsing_manga import get_data_manga
import markup as kup


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")  # То что будет после написания /start
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Игорь, здравствуйте!\nВыберете категорию новостей!!", reply_markup=kup.keyboard)  # Моментальный ответ в чат!!


#-------------------ANIME------------------------#

@dp.message_handler(Text(equals="Аниме"))  # То что будет после нажатия на кнопку Аниме
async def get_info_anime(message: types.Message):
    await message.answer("Выберете, что именно вы хотите!", reply_markup=kup.other_menu_anime)


@dp.message_handler(Text(equals='В процессе просмотра'))
async def get_continue_manga(message: types.Message):
    await message.answer("Подождите пожалуйста...")

    get_data_anime()

    with open("JSON_FAILS/info_anime.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:  # Создание карточек с нужной информацией
        card = f"{hbold('Название: ')} {item['Название']}\n" \
               f"{hbold('Серии: ')} {item['Добавленные серии']}/{item['Все серии']}\n" \
               f"{hlink(item['Ссылка'], item['Ссылка'])}"

        await message.answer(card)


@dp.message_handler(Text(equals="Запланированные"))
async def get_new_manga(message: types.Message):
    await message.answer("Подождите пожалуйста...")

    get_data_anime()

    with open("JSON_FAILS/info_anime.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:  # Создание карточек с нужной информацией
        card = f"{hbold('Название: ')} {item['Название']}\n" \
               f"{hbold('Серии: ')} {item['Добавленные серии']}/{item['Все серии']}\n" \
               f"{hlink(item['Ссылка'], item['Ссылка'])}"

        await message.answer(card)


#-------------------FILMS------------------------#

@dp.message_handler(Text(equals="Фильмы"))
async def get_info_films(message: types.Message):
    await message.answer("Подождите пожалуйста...")

    get_data_film()

    with open("JSON_FAILS/info_films.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        card = f"{hbold('Название: ')} {item['Название']}\n" \
            f"{hbold('Рейтинг: ')} {item['Рейтинг']}\n" \
            f"{hbold('Год выхода: ')} {item['Год выхода']}\n" \
            f"{hbold('Режиссёр: ')} {item['Режиссёр']}\n" \
            f"{hbold('Страна: ')} {item['Страна']}\n" \
            f"{hlink(item['Ссылка'], item['Ссылка'])}"

        await message.answer(card)


#-------------------MANGA------------------------#

@dp.message_handler(Text(equals="Манга"))
async def get_info_manga(message: types.Message):
    await message.answer("Выберете, что именно вы хотите!", reply_markup=kup.other_menu_manga)


@dp.message_handler(Text(equals='Прочитанные, но ещё выходящие'))
async def get_continue_manga(message: types.Message):
    await message.answer("Подождите пожалуйста...")

    get_data_manga()

    with open("JSON_FAILS/info_manga.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        card = f"{hbold('Название: ')} {item['Название']}\n" \
            f"{hbold('Количество томов и глав: ')} {item['Количество томов и глав']}\n" \
            f"{hbold('Перевод: ')} {item['Перевод']}\n" \
            f"{hlink(item['Ссылка'], item['Ссылка'])}"

        await message.answer(card)


@dp.message_handler(Text(equals="То что хочу начать"))
async def get_new_manga(message: types.Message):
    await message.answer("Подождите пожалуйста...")

    get_data_manga()

    with open("JSON_FAILS/info_manga.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        card = f"{hbold('Название: ')} {item['Название']}\n" \
               f"{hbold('Количество томов и глав: ')} {item['Количество томов и глав']}\n" \
               f"{hbold('Перевод: ')} {item['Перевод']}\n" \
               f"{hlink(item['Ссылка'], item['Ссылка'])}"

        await message.answer(card)


#-------------------BACK MENU------------------------#

@dp.message_handler(Text(equals="Назад"))
async def get_new_manga(message: types.Message):
    await message.answer("Вы можете вернуться назад!", reply_markup=kup.keyboard)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
