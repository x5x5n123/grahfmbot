import telebot
from telebot import types

TOKEN = "6493655843:AAGDKLxZoqJ61JquPA5CewB24zqyvRTQG-8"
bot = telebot.TeleBot(TOKEN)

ADMIN_USERNAME = '@x5x5n'

@bot.message_handler(commands=['start', 'ابدأ'])
def send_welcome(message):
    name = message.from_user.first_name
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn1 = types.InlineKeyboardButton('ارقام VIP', callback_data='numbers')
    btn2 = types.InlineKeyboardButton('رشق ملكي ', callback_data='boost')
    btn3 = types.InlineKeyboardButton('فك الحظر', callback_data='unban')
    btn4 = types.InlineKeyboardButton('حظر تأديبي', callback_data='ban')
    btn5 = types.InlineKeyboardButton('تواصل مع الزعيم', url='https://t.me/x5x5n')
    btn6 = types.InlineKeyboardButton('العروض الخاصة', callback_data='offers')
    
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    
    welcome_text = f"🔥 *يا حياك الله {name}* 🔥\n\n⚔️ ═════════ 👑 ═════════ ⚔️\n*بوت الجراح شبل إب*\n*أقوى بوت في اليمن 🇾🇪*\n*رقم 1 بلا منازع 💯*\n⚔️ ═════════ 👑 ═════════ ⚔️\n\n*وصلت لعريش الخدمات الرقمية* 😎👇\n*هنا الملوك والأساطير فقط*\n\n*خدماتنا الجبارة:*\n- *أرقام وهمية VIP* لكل دول العالم\n- رشق متابعين يخليك ترند بدقايق\n- فك حظر المستحيل عندنا سهل\n- حظر فوري لأي مزعج أو سبام\n\n*الجراح شبل إب = هيبة + ثقة + ضمان*\n*الجودة*"
    
    bot.reply_to(message, welcome_text, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    bot.answer_callback_query(call.id, "قريباً... تواصل مع @x5x5n")

print("Bot is running...")
bot.infinity_polling()- رشق متابعين يخليك ترند بدقايق
- فك حظر المستحيل عندنا سهل
- حظر فوري لأي مزعج أو سبام

*الجراح شبل إب = هيبة + ثقة + ضمان*
*الجودة*
"""
    
    bot.reply_to(message, welcome_text, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'numbers':
        bot.answer_callback_query(call.id, "قريباً... تواصل مع @x5x5n")
    elif call.data == 'boost':
        bot.answer_callback_query(call.id, "قريباً... تواصل مع @x5x5n")
    elif call.data == 'unban':
        bot.answer_callback_query(call.id, "قريباً... تواصل مع @x5x5n")
    elif call.data == 'ban':
        bot.answer_callback_query(call.id, "قريباً... تواصل مع @x5x5n")
    elif call.data == 'offers':
        bot.answer_callback_query(call.id, "قريباً... تواصل مع @x5x5n")

print("Bot is running...")
bot.infinity_polling()- رشق متابعين يخليك ترند بدقايق
- فك حظر المستحيل عندنا سهل
- حظر فوري لأي مزعج أو سبام

*الجراح شبل إب = هيبة + ثقة + ضمان*
"""
    
    bot.reply_to(message, welcome_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'numbers':
        bot.answer_callback_query(call.id, "قريباً... تواصل مع @x5x5n")
    elif call.data == 'boost':
        bot.answer_callback_query(call.id, "قريباً... تواصل مع @x5x5n")
    elif call.data == 'unban':
        bot.answer_callback_query(call.id, "قريباً... تواصل مع @x5x5n")
    elif call.data == 'ban':
        bot.answer_callback_query(call.id, "قريباً... تواصل مع @x5x5n")
    elif call.data == 'offers':
        bot.answer_callback_query(call.id, "قريباً... تواصل مع @x5x5n")

print("Bot is running...")
bot.infinity_polling() رشق متابعين يخليك ترند بدقايق
 فك حظر المستحيل عندنا سهل
 حظر فوري لأي مزعج أو سبام

*الجراح شبل إب = هيبة + ثقة + ضمان* 
*الجودة*
''', reply_markup=markup)

print("Bot is running...")
bot.infinity_polling()
*خدماتنا الجبارة:*
 *أرقام وهمية VIP* لكل دول العالم
 رشق متابعين يخليك ترند بدقايق
 فك حظر المستحيل عندنا سهل
 حظر فوري لأي مزعج أو سبام

*الجراح شبل إب = هيبة + ثقة + ضمان* 
*الجودة*
''', reply_markup=markup)

print("Bot is running...")
bot.infinity_polling()
