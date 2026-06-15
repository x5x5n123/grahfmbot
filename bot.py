import telebot
from telebot import types

TOKEN = "6493655843:AAGDKLxZoqJ61JquPA5CewB24zqyvRTQG-8"
bot = telebot.TeleBot(TOKEN)

ADMIN_USERNAME = '@x5x5n'

# ========== القائمة الرئيسية ==========
@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton('🔥 ارقام VIP', callback_data='numbers'),
        types.InlineKeyboardButton('⚡ رشق ملوكي', callback_data='boost'),
        types.InlineKeyboardButton('🔓 فك الحظر', callback_data='unban'),
        types.InlineKeyboardButton('🔨 حظر تأديبي', callback_data='ban'),
        types.InlineKeyboardButton('💎 العروض الخاصة', callback_data='offers'),
        types.InlineKeyboardButton('👑 تواصل مع الزعيم', url='https://t.me/x5x5n')
    )
    text = "🔥 *يا حياك الله " + name + "* 🔥\n\n"
    text = text + "⚔️ ═════════ 👑 ═════════ ⚔️\n"
    text = text + "*بوت الجراح شبل إب*\n"
    text = text + "*أقوى بوت في اليمن 🇾🇪*\n"
    text = text + "*رقم 1 بلا منازع 💯*\n"
    text = text + "⚔️ ═════════ 👑 ═════════ ⚔️\n\n"
    text = text + "*وصلت لعريش الخدمات الرقمية* 😎👇\n"
    text = text + "*هنا الملوك والأساطير فقط*\n\n"
    text = text + "*الجراح شبل إب = هيبة + ثقة + ضمان*"
    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode='Markdown')

# ========== معالج الأزرار ==========
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'main_menu':
        start(call.message)
    
    # 1. قائمة الأرقام
    elif call.data == 'numbers':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('🇺🇸 امريكا - 3$ | 3 شهور ضمان', callback_data='num_us'),
            types.InlineKeyboardButton('🇬🇧 بريطانيا - 4$ | VIP', callback_data='num_uk'),
            types.InlineKeyboardButton('🇷🇺 روسيا - 2.5$ | تفعيل فوري', callback_data='num_ru'),
            types.InlineKeyboardButton('🇸🇦 السعودية - 5$ | خاص واتساب', callback_data='num_sa'),
            types.InlineKeyboardButton('🌍 دول أخرى - 2$ وطالع', callback_data='num_other'),
            types.InlineKeyboardButton('🔙 رجوع للقائمة الرئيسية', callback_data='main_menu')
        )
        text = "🔥 *قسم الأرقام الوهمية VIP* 🔥\n\n"
        text = text + "⚜️ *أرقام نظيفة 100% غير محروقة*\n"
        text = text + "⚜️ *ضمان استبدال لو ما اشتغل*\n"
        text = text + "⚜️ *تفعيل جميع التطبيقات: واتساب + تيليجرام + انستا*\n\n"
        text = text + "*اختر الدولة المطلوبة:* 👇"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
    
    # 2. قائمة الرشق
    elif call.data == 'boost':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('📸 انستقرام', callback_data='boost_insta'),
            types.InlineKeyboardButton('🎵 تيك توك', callback_data='boost_tiktok'),
            types.InlineKeyboardButton('✈️ تيليجرام', callback_data='boost_telegram'),
            types.InlineKeyboardButton('🔙 رجوع للقائمة الرئيسية', callback_data='main_menu')
        )
        text = "⚡ *قسم الرشق الملكي* ⚡\n\n"
        text = text + "👑 *متابعين حقيقيين + ضمان تعويض*\n"
        text = text + "👑 *بدء التنفيذ خلال 5 دقايق*\n"
        text = text + "👑 *أرخص سعر بالسوق + جودة أسطورية*\n\n"
        text = text + "*اختر المنصة:* 👇"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

    # 2.1 رشق انستقرام
    elif call.data == 'boost_insta':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1000 متابع = 2$ 🔥', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('5000 متابع = 8$ 💎 عرض', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('10K متابع = 15$ 👑 الأقوى', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('100K لايك = 5$ ⚡', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('🔙 رجوع', callback_data='boost')
        )
        text = "📸 *رشق انستقرام* 📸\n\n"
        text = text + "*الأسعار:*\n"
        text = text + "▪️ متابعين عرب متفاعلين + ضمان 30 يوم\n"
        text = text + "▪️ لايكات + مشاهدات ستوري + تعليقات\n"
        text = text + "▪️ *ملاحظة:* الحساب لازم يكون عام\n\n"
        text = text + "*للطلب اضغط على الباقة وتواصل مع الزعيم* 👇"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

    # 2.2 رشق تيك توك
    elif call.data == 'boost_tiktok':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1000 متابع = 2.5$ 🔥', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('10K لايك = 3$ 💎', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('100K مشاهدة = 1$ ⚡ جنون', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('🔙 رجوع', callback_data='boost')
        )
        text = "🎵 *رشق تيك توك* 🎵\n\n"
        text = text + "*عروض اليوم:*\n"
        text = text + "▪️ متابعين يرفعونك اكسبلور\n"
        text = text + "▪️ لايكات سريعة ما تنقص\n"
        text = text + "▪️ مشاهدات تخلي فيديوك ترند\n\n"
        text = text + "*اضغط للطلب المباشر* 👇"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

    # 2.3 رشق تيليجرام
    elif call.data == 'boost_telegram':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1000 عضو = 3$ 👑 قنوات', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('1000 عضو = 4$ 🔥 قروبات', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('10K مشاهدة = 1$ ⚡ للبوست', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('🔙 رجوع', callback_data='boost')
        )
        text = "✈️ *رشق تيليجرام* ✈️\n\n"
        text = text + "*الخدمات:*\n"
        text = text + "▪️ أعضاء قنوات + قروبات ضمان عدم النقص\n"
        text = text + "▪️ مشاهدات بوست آخر 5 منشورات\n"
        text = text + "▪️ تفاعل + تصويت\n\n"
        text = text + "*للطلب الفوري* 👇"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

    # 3. فك الحظر
    elif call.data == 'unban':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('🔓 واتساب - 10$ | مضمون', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('📸 انستقرام - 15$ | حتى المعطل', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('✈️ تيليجرام - 8$ | فوري', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('🔙 رجوع للقائمة الرئيسية', callback_data='main_menu')
        )
        text = "🔓 *قسم فك الحظر* 🔓\n\n"
        text = text + "⚠️ *نفك المستحيل بإذن الله*\n"
        text = text + "⚠️ *الدفع بعد الفك للثقة*\n"
        text = text + "⚠️ *حظر أرقام + حسابات + أجهزة*\n\n"
        text = text + "*اختر نوع الحظر:* 👇"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

    # 4. حظر تأديبي
    elif call.data == 'ban':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('🔨 حظر واتساب - 7$ | يطير بدقايق', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('🔨 حظر انستا - 12$ | نهائي', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('🔙 رجوع للقائمة الرئيسية', callback_data='main_menu')
        )
        text = "🔨 *قسم الحظر التأديبي* 🔨\n\n"
        text = text + "⚔️ *للمزعجين والنصابين والسبام فقط*\n"
        text = text + "⚔️ *نستخدم طرق خاصة ما تنفك*\n"
        text = text + "⚔️ *الدفع مقدم + إثبات قبل وبعد*\n\n"
        text = text + "*اختر المنصة:* 👇"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

    # 5. العروض الخاصة
    elif call.data == 'offers':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('🎁 باقة التاجر 50$ = رقم + 10K متابع', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('🎁 باقة المشاهير 100$ = شامل كل شي', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('👑 تواصل مع الزعيم للعروض الخاصة', url='https://t.me/x5x5n'),
            types.InlineKeyboardButton('🔙 رجوع للقائمة الرئيسية', callback_data='main_menu')
        )
        text = "💎 *العروض الخاصة - لفترة محدودة* 💎\n\n"
        text = text + "*1. باقة التاجر 50$*\n"
        text = text + "رقم امريكي VIP + 10K متابع انستا + 50K مشاهدة تيك توك\n\n"
        text = text + "*2. باقة المشاهير 100$*\n"
        text = text + "رقم + 25K متابع انستا + 10K تيليجرام + فك حظر مجاني مرة\n\n"
        text = text + "*للطلب اضغط على الباقة* 👇"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

    # ردود الأرقام
    elif call.data.startswith('num_'):
        bot.answer_callback_query(call.id, "للطلب اضغط زر التواصل مع الزعيم 👑", show_alert=True)

bot.infinity_polling()
