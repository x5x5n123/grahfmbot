import telebot
from telebot import types

TOKEN = "6493655843:AAGDKLxZoqJ61JquPA5CewB24zqyvRTQG-8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton('ارقام VIP', callback_data='numbers'),
        types.InlineKeyboardButton('رشق ملوكي', callback_data='boost'),
        types.InlineKeyboardButton('فك الحظر', callback_data='unban'),
        types.InlineKeyboardButton('حظر تأديبي', callback_data='ban'),
        types.InlineKeyboardButton('تواصل مع الزعيم', url='https://t.me/x5x5n'),
        types.InlineKeyboardButton('العروض الخاصة', callback_data='offers')
    )
    text = "يا حياك الله " + name + "\n\n"
    text = text + "بوت الجراح شبل إب\n"
    text = text + "أقوى بوت في اليمن\n"
    text = text + "رقم 1 بلا منازع\n\n"
    text = text + "وصلت لعريش الخدمات الرقمية\n"
    text = text + "هنا الملوك والأساطير فقط\n\n"
    text = text + "خدماتنا:\n"
    text = text + "- أرقام وهمية VIP لكل دول العالم\n"
    text = text + "- رشق متابعين يخليك ترند بدقايق\n"
    text = text + "- فك حظر المستحيل عندنا سهل\n"
    text = text + "- حظر فوري لأي مزعج أو سبام\n\n"
    text = text + "الجراح شبل إب = هيبة + ثقة + ضمان"
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query(call.id, "قريباً... تواصل مع @x5x5n")

bot.infinity_polling()
