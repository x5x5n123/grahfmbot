import telebot
from telebot import types

# التوكن الجديد حقك
TOKEN = "6493655843:AAGDKLxZoqJ61JquPA5CewB24zqyvRTQG-8"
bot = telebot.TeleBot(TOKEN)

# يوزرك حق الدعم
ADMIN_USERNAME = '@x5x5n'

# أمر start/
@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn1 = types.InlineKeyboardButton('📱💯 أرقام VIP', callback_data='numbers')
    btn2 = types.InlineKeyboardButton('🚀🔥 رشق ملوكي', callback_data='boost')
    btn3 = types.InlineKeyboardButton('🔓👑 فك الحظر', callback_data='unban')
    btn4 = types.InlineKeyboardButton('⛔⚔️ حظر تأديبي', callback_data='ban')
    btn5 = types.InlineKeyboardButton('💬🫡 تواصل مع الزعيم', url='https://t.me/x5x5n')
    btn6 = types.InlineKeyboardButton('⭐🎖️ العروض الخاصة', callback_data='offers')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

    bot.reply_to(message, f'''
🔥 *حياك الله يا {name}* 🔥

⚔️ ════════ 👑 ════════ ⚔️
   *بوت الجراح شبل إب*
  *أقوى بوت في اليمن 🇾🇪*
  *رقم 1 بلا منازع 💯*
⚔️ ════════ 👑 ════════ ⚔️

*وصلت لعرش الخدمات الرقمية* 😎🫡
*هنا الملوك والأساطير فقط*

*خدماتنا الجبارة:*
💎 *أرقام وهمية VIP* لكل دول العالم
💎 *رشق متابعين* يخليك ترند بدقايق
💎 *فك حظر* المستحيل عندنا سهل
💎 *حظر فوري* لأي مزعج أو سبام

*الجراح شبل إب = هيبة + ثقة + ضمان* 🛡️
*الجودة
