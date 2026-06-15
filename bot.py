import telebot
from telebot import types

# التوكن حقك
TOKEN = '6493655843:AAE5ZLzLqEnHq_8ffqamdeV87_q_vn_DONQ'
bot = telebot.TeleBot(TOKEN)

# يوزرك حق الدعم
ADMIN_USERNAME = '@x5x5n' 

# أمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn1 = types.InlineKeyboardButton('📱 أرقام وهمية', callback_data='numbers')
    btn2 = types.InlineKeyboardButton('🚀 رشق متابعين', callback_data='boost')
    btn3 = types.InlineKeyboardButton('🔓 فك حظر', callback_data='unban')
    btn4 = types.InlineKeyboardButton('⛔️ حظر أرقام', callback_data='ban')
    btn5 = types.InlineKeyboardButton('💬 تواصل مع الإدارة', url='https://t.me/x5x5n')
    
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    bot.reply_to(message, f'''
أهلاً {name} 👋

🔥 بوت الجراح شبل إب 🇾🇪 🔥
لجميع خدمات التيليجرام والسوشيال ميديا

⚡️ أرقام وهمية لجميع الدول
⚡️ رشق متابعين انستا + تيك توك + تيليجرام
⚡️ فك حظر الأرقام واليوزرات
⚡️ خدمات حظر

اختر الخدمة من الأزرار:
''', reply_markup=markup)

# الأزرار
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'numbers':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f'''
📱 *قسم الأرقام الوهمية*

الدول المتوفرة:
🇺🇸 أمريكا | 🇬🇧 بريطانيا | 🇸🇦 السعودية
🇪🇬 مصر | 🇦🇪 الإمارات | وغيرها...

الأسعار تبدأ من 0.5$

للطلب تواصل مع الإدارة: {ADMIN_USERNAME}
''', parse_mode='Markdown')
        
    elif call.data == 'boost':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f'''
🚀 *قسم الرشق*

1. متابعين تيليجرام
2. متابعين انستقرام 
3. متابعين تيك توك
4. مشاهدات + لايكات

أرخص الأسعار وأسرع تنفيذ ⚡️

للطلب تواصل مع الإدارة: {ADMIN_USERNAME}
''', parse_mode='Markdown')
        
    elif call.data == 'unban':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f'''
🔓 *خدمة فك الحظر*

نفك حظر:
- أرقام التيليجرام
- يوزرات تيليجرام
- أرقام واتساب

ارسل الرقم أو اليوزر المحظور للإدارة: {ADMIN_USERNAME}
''', parse_mode='Markdown')
        
    elif call.data == 'ban':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f'''
⛔️ *خدمة الحظر*

نوفر حظر:
- أرقام مزعجة
- يوزرات سبام

للتنفيذ تواصل مع الإدارة: {ADMIN_USERNAME}
''', parse_mode='Markdown')

# أمر /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, f'للطلب والاستفسار تواصل مع الإدارة: {ADMIN_USERNAME}')

# أي رسالة ثانية
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'استخدم /start عشان تشوف قائمة الخدمات')

print("البوت شغال...")
bot.infinity_polling()