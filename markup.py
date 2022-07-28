from aiogram import types

# --- Main Menu ---
start_buttons = ["Аниме", "Фильмы", "Манга"]  # Название кнопок в главном меню
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Вывод меню под местом для печати + уменьшенные иконки
keyboard.add(*start_buttons)  # Добавление кнопок в главное меню

# --- Other Menu Manga ---
other_buttons_manga = ['Прочитанные, но ещё выходящие', 'То что хочу начать', 'Назад']
other_menu_manga = types.ReplyKeyboardMarkup(resize_keyboard=True)
other_menu_manga.add(*other_buttons_manga)

# --- Back manga ---
back_buttons_manga = ['Назад']
back_menu_manga = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_menu_manga.add(*back_buttons_manga)

# --- Other Menu Anime ---
other_buttons_anime = ['В процессе просмотра', 'Запланированные', 'Назад']
other_menu_anime = types.ReplyKeyboardMarkup(resize_keyboard=True)
other_menu_anime.add(*other_buttons_anime)

# --- Back anime ---
back_buttons_anime = ['Назад']
back_menu_anime = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_menu_anime.add(*back_buttons_anime)
