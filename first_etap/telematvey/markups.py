from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


BtnMain = KeyboardButton("⬅️Главное меню")

# ___Main menu___
spButton = KeyboardButton('🥊Спорт')
edButton = KeyboardButton("🎓Образование")
enButton = KeyboardButton("🎳Развлечения")
hwButton = KeyboardButton("🧹Работа по дому")
krButton = KeyboardButton("📝Создать свое задание")
lolButton = KeyboardButton("➡️Прочее")
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(spButton,edButton,enButton,hwButton,krButton,lolButton)



# ___Other menu___
hpButton = KeyboardButton('✋Помощь')
dsButton = KeyboardButton('📃Описание бота')
stButton = KeyboardButton('🐈Стикер котика')
other_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(hpButton, dsButton, stButton, BtnMain)


# ___inline menu___
ik1 = InlineKeyboardButton(text="Выполнить 👍", callback_data="get")
ik2 = InlineKeyboardButton(text="Забросить 👎", callback_data="pass")
ikb = InlineKeyboardMarkup(row_width=2).add(ik1, ik2)
