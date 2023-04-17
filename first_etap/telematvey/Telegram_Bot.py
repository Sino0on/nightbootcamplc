from aiogram import Bot, Dispatcher, types, executor
from random import choice
import markups as nav
import json
import config

bot = Bot(config.bot_token)
dp = Dispatcher(bot)



async def on_startup(_):                                 # Проверка бота на запуске
    print('Бот был успешно запущен!')



@dp.message_handler(commands=['start'])                          # Хандлер отвечает за старт бота
async def echo_starter(messege: types.Message):
    await bot.send_photo(chat_id=messege.chat.id,
                         photo="https://img.championat.com/i/n/j/16546005982003863007.jpg",
                         caption="Что вы будете делать сегодня?", reply_markup=nav.main_menu)
    await messege.delete()



@dp.message_handler(commands=['help'])                          # Хандлер выдает список всех комманд
async def echo_helper(messege: types.Message):
    await messege.reply(text=config.helper)
    await messege.delete()



@dp.message_handler(commands=['description'])                     # Хандлер вызывает описание бота
async def echo_descriptioner(messege: types.Message):
    await messege.answer(text=config.des)
    await messege.delete()



@dp.message_handler(commands=['sticker'])            # Хандлер отвечающий за стикер кота
async def get_sticker(messege: types.Message):
    with open("database.json", "r") as f:
        data = json.load(f)
        sticker = choice(data["sticker"])
    await bot.send_sticker(messege.from_user.id, sticker=sticker)
    await messege.delete()



@dp.message_handler()
async def bot_messege(messege: types.Message):
    with open('database.json', 'r') as f:
        data = json.load(f)
    if messege.text == "🥊Спорт":              # Выдает рандомное задание из списка Спорт
        with open("database.json", "r") as f:
            data = json.load(f)
            sport = choice(data["sport"])
        try:
            await bot.send_photo(chat_id=messege.chat.id, photo=sport[1], caption=sport[0],
                                 reply_markup=nav.ikb)
            await messege.delete()
        except:                                         # Если нет действительного адреса фотографии
            await bot.send_photo(chat_id=messege.chat.id, photo=config.phot, caption=sport[0],
                                 reply_markup=nav.ikb)
            await messege.delete()

    elif messege.text == "🎓Образование":                     # Выдает рандомное задание из списка Образование
        with open("database.json", "r", encoding='utf8') as f:
            data = json.load(f)
            education = choice(data["education"])
        try:
            await bot.send_photo(chat_id=messege.chat.id, photo=education[1], caption=education[0],
                                 reply_markup=nav.ikb)
            await messege.delete()
        except:
            await bot.send_photo(chat_id=messege.chat.id, photo=config.phot, caption=education[0],
                                 reply_markup=nav.ikb)
            await messege.delete()

    elif messege.text == "🎳Развлечения":                       # Выдает рандомное задание из списка Развллечения
        with open("database.json", "r") as f:
            data = json.load(f)
            entertainments = choice(data["entertainments"])
            try:
                await bot.send_photo(chat_id=messege.chat.id, photo=entertainments[1], caption=entertainments[0],
                                     reply_markup=nav.ikb)
                await messege.delete()
            except:
                await bot.send_photo(chat_id=messege.chat.id, photo=config.phot, caption=entertainments[0],
                                     reply_markup=nav.ikb)
                await messege.delete()


    elif messege.text == "🧹Работа по дому":                          # Выдает рандомное задание из списка Работа по дому
        with open("database.json", "r") as f:
            data = json.load(f)
            housework = choice(data["housework"])
        try:
            await bot.send_photo(chat_id=messege.chat.id, photo=housework[1], caption=housework[0],
                                 reply_markup=nav.ikb)
            await messege.delete()
        except:
            await bot.send_photo(chat_id=messege.chat.id, photo=config.phot, caption=housework[0],
                                 reply_markup=nav.ikb)
            await messege.delete()

    elif messege.text == '📝Создать свое задание':
        await bot.send_photo(chat_id=messege.chat.id,
                             photo='https://thumbs.dreamstime.com/z/sorry-having-technical-difficulties-message-yellow-sign-message-isolated-white-technical-difficulties-message-215071343.jpg',
                             caption=f'Чтобы создать задание вам нужно написать слово "Создать" и через пробел написать описание задания и через category указать категорию и потом через "url=" передать ссылку на фото \n{data.keys()}')
        await messege.delete()

    elif messege.text == '➡️Прочее':                                # переход в другое меню
        await messege.answer(text=messege.text, reply_markup=nav.other_menu)
        await messege.delete()

    elif messege.text == '✋Помощь':                      # Выдает список комманд
        await messege.reply(text=config.helper)
        await messege.delete()

    elif messege.text == "📃Описание бота":                 # Выдает описание бота
        await messege.answer(text=config.des, parse_mode="HTML")
        await messege.delete()

    elif messege.text == "🐈Стикер котика":
        with open("database.json", "r") as f:
            data = json.load(f)
            sticker = choice(data["sticker"])
        await bot.send_sticker(messege.from_user.id, sticker=sticker)
        await messege.delete()

    elif messege.text == "⬅️Главное меню":
        await messege.answer(text=messege.text, reply_markup=nav.main_menu)
        await messege.delete()
    elif 'Создать' in messege.text:
        category = messege.text.split('category=')[-1].split(' ')[0]
        image = messege.text.split('url=')[-1]
        description = messege.text.split('Создать')[-1].split('category')[0]
        data[category].append([description, image])
        with open('database.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)
        await messege.answer('Успешно было добавлено ваше задание')




@dp.callback_query_handler()                            # Обработка ответов
async def task_answer(callback: types.CallbackQuery):
    if callback.data == "get":
        await callback.answer(text="Вы выполнили задание, Молодец! 👍")
    elif callback.data == "pass":
        await callback.answer(text="Вы неудачник, не смогли выполнить даже такое простое задание! 👎")




if __name__ == "__main__":                             # Запуск бота
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)