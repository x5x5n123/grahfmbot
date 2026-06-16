import os
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive"

# قائمة الدول كاملة مع الأسعار
COUNTRIES = {
    "page1": [
        ["🇺🇸 امريكا - $3 | 3 شهور ضمان", "usa"],
        ["🇬🇧 بريطانيا - $4 | VIP", "uk"],
        ["🇷🇺 روسيا - $2.5 | تفعيل فوري", "ru"],
        ["🇸🇦 السعودية - $5 | خاص واتساب", "sa"],
        ["🇦🇪 الامارات - $4.5", "ae"],
        ["🇰🇼 الكويت - $4", "kw"],
        ["🇶🇦 قطر - $4", "qa"],
        ["🇧🇭 البحرين - $3.5", "bh"],
    ],
    "page2": [
        ["🇴🇲 عمان - $3.5", "om"],
        ["🇪🇬 مصر - $2", "eg"],
        ["🇾🇪 اليمن - $2.5", "ye"],
        ["🇯🇴 الأردن - $2.5", "jo"],
        ["🇱🇧 لبنان - $3", "lb"],
        ["🇮🇶 العراق - $2", "iq"],
        ["🇲🇦 المغرب - $2", "ma"],
        ["🇩🇿 الجزائر - $2", "dz"],
    ],
    "page3": [
        ["🇹🇳 تونس - $2", "tn"],
        ["🇱🇾 ليبيا - $2.5", "ly"],
        ["🇸🇩 السودان - $2", "sd"],
        ["🇸🇾 سوريا - $3", "sy"],
        ["🇵🇸 فلسطين - $2.5", "ps"],
        ["🇹🇷 تركيا - $2", "tr"],
        ["🇮🇷 ايران - $2.5", "ir"],
        ["🇵🇰 باكستان - $1.5", "pk"],
    ],
    "page4": [
        ["🇮🇳 الهند - $1.2", "in"],
        ["🇧🇩 بنجلاديش - $1.5", "bd"],
        ["🇮🇩 اندونيسيا - $1.8", "id"],
        ["🇲🇾 ماليزيا - $2", "my"],
        ["🇵🇭 الفلبين - $1.5", "ph"],
        ["🇹🇭 تايلاند - $2", "th"],
        ["🇻🇳 فيتنام - $1.8", "vn"],
        ["🇨🇳 الصين - $2.5", "cn"],
    ],
    "page5": [
        ["🇯🇵 اليابان - $3", "jp"],
        ["🇰🇷 كوريا الجنوبية - $3", "kr"],
        ["🇩🇪 المانيا - $3.5", "de"],
        ["🇫🇷 فرنسا - $3.5", "fr"],
        ["🇪🇸 اسبانيا - $3", "es"],
        ["🇮🇹 ايطاليا - $3", "it"],
        ["🇳🇱 هولندا - $3", "nl"],
        ["🇧🇪 بلجيكا - $3", "be"],
    ],
    "page6": [
        ["🇨🇦 كندا - $3.5", "ca"],
        ["🇲🇽 المكسيك - $2.5", "mx"],
        ["🇧🇷 البرازيل - $2.5", "br"],
        ["🇦🇷 الارجنتين - $2.5", "ar"],
        ["🇿🇦 جنوب افريقيا - $2", "za"],
        ["🇳🇬 نيجيريا - $1.5", "ng"],
        ["🇰🇪 كينيا - $1.5", "ke"],
        ["🌍 باقي الدول - $2", "other"],
    ]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    first_name = user.first_name
    user_id = user.id
    bot_name = "جراف | GRAHF"

    text = f"""
🏰 - مرحبا بك في القائمة الرئيسية ✅
⚜️ - لدى بوت {bot_name} | SMS العالمي

- اهلا بك عزيزي : {first_name} ❤️
- حسابك : {user_id}@GRAHF.com 📮
- رصيد حسابك الان : 0.0 $ 💰
- اخر الاخبار ⬇️

❤️😍 اسعار الشحن في البوت انقر للعرض
- تحكم الان بضغط على الازرار بلاسفل ⬇️
    """

    keyboard = [
        [InlineKeyboardButton("• 👥 الرشق والحسابات التليجرام •", callback_data="boost")],
        [
            InlineKeyboardButton("🚀 عروض تليجرام 🔥", callback_data="tg_offers"),
            InlineKeyboardButton("🎁 عروض الواتساب 🚀", callback_data="wa_offers")
        ],
        [InlineKeyboardButton("• 📞 شراء أرقام لتطبيقات اخرا 📞 •", callback_data="numbers")],
        [
            InlineKeyboardButton("💰 شحن حسابك •", callback_data="charge"),
            InlineKeyboardButton("• 📋 سجل الحساب ✔️", callback_data="history")
        ],
        [InlineKeyboardButton("• 💬 الاكثر توفراً واتساب •", callback_data="whatsapp")],
        [
            InlineKeyboardButton("⚠️ طلب المساعدة •", callback_data="help"),
            InlineKeyboardButton("• 🌟 خدمات ومميزات 🌟", callback_data="features")
        ],
        [InlineKeyboardButton("• 💵 مشاركة رابط الدعوة الخاص بك 🔵", callback_data="ref")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)

async def show_countries(update: Update, context: ContextTypes.DEFAULT_TYPE, page="page1"):
    query = update.callback_query

    text = """
🔥 قسم الأرقام الوهمية VIP

أرقام نظيفة 100% غير محروقة ⚜️
ضمان استبدال لو ما اشتغل ⚜️
تفعيل جميع التطبيقات: واتساب + تيليجرام + انستا ⚜️

👇 اختر الدولة المطلوبة:
    """

    keyboard = []
    for country_name, country_code in COUNTRIES[page]:
        keyboard.append([InlineKeyboardButton(country_name, callback_data=f"buy_{country_code}")])

    # أزرار التنقل بين الصفحات
    nav_buttons = []
    pages = list(COUNTRIES.keys())
    current_index = pages.index(page)

    if current_index > 0:
        nav
