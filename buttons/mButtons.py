from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton



main_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_btn.add("📊Statistika", "🔧Kanallar", "📤Reklama", "♻️ Tozalash")

channel_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
channel_btn.add("➕Kanal qo'shish", "❌Kanalni olib tashlash")
channel_btn.add("📋 Kanallar ro'yxati", "🔙Orqaga qaytish")

reklama_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
reklama_btn.add("📨Forward xabar yuborish", "📬Oddiy xabar yuborish", "🔙Orqaga qaytish")


frond_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
frond_btn.add('📕BAKALAVRIAT 2022', "📘O'qishni ko'chirish️")

qabul_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
qabul_btn.add("〽️Natija uchun", '📝Baxolash mezonlari', "⏪Orqaga qaytish")

orqagaBtn = ReplyKeyboardMarkup(resize_keyboard=True)
orqagaBtn.add("⏪Orqaga qaytish")

transfer_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
transfer_btn.add("〽Natija️")
transfer_btn.add("📝Baxolash mezonlari️", "💰Super kontrakt miqdori️", "⏪Orqaga qaytish")