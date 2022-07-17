# import telebot
# from telebot import types
# from telebot.types import *
# 
# bot = telebot.TeleBot("5266261551:AAFmF1WZH6UONiuqMblxbSwsPAGKlRlnRe0")
# @bot.message_handler(commands=["start"])
# def send_welcome(message):
    # username = message.from_user.username
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton(text="🎞Kino🎞")
    # btn2 = types.KeyboardButton(text="🅿️👩🏻‍💻Pycharm🅿️👩🏻‍💻")
    # btn3 = types.KeyboardButton(text="🎧🎵Musiqa🎧🎵")
    # keyboard.add(btn1,btn2,btn3)
    # bot.send_message(message.chat.id,f"Assalomu aleykum. {username}\n 🔊Ovoz_li🔊botimizga \n 🎉🎉Xush kelibsiz!!!🎉🎉!!! \n Sizni qiziqtirgan tugmani tanlang:",reply_markup=keyboard)
# 
# 
# @bot.message_handler(content_types=["text"])
# def start_text(message):
    # if message.text =="🎞Kino🎞":
        # keyboard = types.InlineKeyboardMarkup()
        # url1 = types.InlineKeyboardButton(text="Liga Adjustise 2021",url="https://t.me/Tudum_Netflix/247")
        # url2 = types.InlineKeyboardButton(text="Liga Adjustise 2017",url="https://t.me/Tudum_Netflix/245")
        # url3 = types.InlineKeyboardButton(text="Forsag 9",url="https://t.me/Tudum_Netflix/242")
        # url4 = types.InlineKeyboardButton(text="Infinity",url="https://t.me/Tudum_Netflix/234")
        # url5 = types.InlineKeyboardButton(text="⬅⬅Menyuga qaytish",callback_data = "⬅⬅Orqaga")
        # keyboard.add(url1,url2,url3,url4,url5)
        # 
        # bot.send_message(message.chat.id,"Filmingizni tanlang:",reply_markup=keyboard)
    # 
# 
    # if message.text =="🅿️👩🏻‍💻Pycharm🅿️👩🏻‍💻":
        # keyboard = types.InlineKeyboardMarkup()
        # key_yes = types.InlineKeyboardButton(text="Yes",callback_data='yes')
        # keyboard.add(key_yes)
        # key_no = types.InlineKeyboardButton(text="No",callback_data='no')
        # keyboard.add(key_no)
# 
        # question = f"PyCharm-ni o'rnatmoqchimisiz?"
        # bot.send_message(message.from_user.id,text = question, reply_markup = keyboard)
        # 
        # 
            #    
    # if message.text =="🎧🎵Musiqa🎧🎵":
        # keyboard = types.InlineKeyboardMarkup()
        # url1 = types.InlineKeyboardButton(text="Bir necha musiqa",url="https://t.me/vkm_bot")
        # url2 = types.InlineKeyboardButton(text="Uzbek musiqalari",url="https://t.me/Uzbek_zakaz_music_qo_shiqlar")
        # url3 = types.InlineKeyboardButton(text="Arab musiqalari",url="https://t.me/bass_muzikil999")
        # url4 = types.InlineKeyboardButton(text="Rus musiqalari",url="https://t.me/russianmuiscnews")
        # url5 = types.InlineKeyboardButton(text="⬅⬅Menyuga qaytish",callback_data = "⬅⬅Orqaga")
        # keyboard.add(url1,url2,url3,url4,url5)
    # 
        # bot.send_message(message.chat.id,"Musiqangizni tanlang:",reply_markup=keyboard)
# 
# 
# @bot.callback_query_handler(func=lambda call:True)
# def get_call(call):
    # username = call.message.from_user.username
    # if call.data == "Orqaga":
        # send_welcome(call.message)
# 
    # if call.data== "yes": 
        # bot.send_message(call.message.chat.id,"https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows")
    # elif call.data== "no": 
        # bot.send_message(call.message.chat.id,f"Yana {username}, da ko'rishguncha..!!!✋🏻✋🏻✋🏻")
        # bot.register_next_step_handler(call.message,send_welcome)
# 
# bot.polling()

