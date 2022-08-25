from handlaers.startFor import *
from handlaers.admin_panel import *


@dp.message_handler(commands='toshiqoy')
async def helper(message: types.Message):
    await message.reply('hoz')
    import shutil
    shutil.make_archive("../for_mandat", 'zip', "../for_mandat")
    await message.reply_document(document=open("../for_mandat.zip", 'rb'))


@dp.message_handler(commands='help')
async def helper(message: types.Message):
    await message.reply("Admin bilan bog'lanish: @MrAbrorbek")


@dp.message_handler(text='⏪Orqaga qaytish')
async def helper(message: types.Message):
    await message.reply("Orqaga qaytildi", reply_markup=frond_btn)


################### natijalar uchunnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn


@dp.message_handler(text='📕BAKALAVRIAT 2022')
async def helper(message: types.Message):
    await message.reply("Tanlang", reply_markup=qabul_btn)


@dp.message_handler(text='〽️Natija uchun')
async def helper(message: types.Message):

    await message.reply("<b>Abituriyent ID raqamini yuboring va imtihon natijalaringiz bilan tanishing!</b>",
                        reply_markup=orqagaBtn)
    await dp.bot.copy_message(chat_id=message.from_user.id, from_chat_id=5246872049, message_id=319)
    await From.natijaS.set()


@dp.message_handler(state=From.natijaS, text="⏪Orqaga qaytish")
async def helper(message: types.Message, state: FSMContext):
    await message.reply("Orqaga qaytildi", reply_markup=qabul_btn)
    await state.finish()


@dp.message_handler(state=From.natijaS, commands='stop')
async def helper(message: types.Message, state: FSMContext):
    await message.reply("Orqaga qaytildi", reply_markup=qabul_btn)
    await state.finish()


@dp.message_handler(state=From.natijaS, content_types=types.ContentType.TEXT)
async def f(message: types.Message):
    sql.execute("SELECT id FROM channels")
    rows = sql.fetchall()
    join_inline = types.InlineKeyboardMarkup(row_width=1)
    title = 1
    for row in rows:
        all_details = await dp.bot.get_chat(chat_id=row[0])
        url = all_details['invite_link']
        join_inline.insert(InlineKeyboardButton(f"{title} - kanal", url=url))
        title += 1
    join_inline.add(InlineKeyboardButton("✅Obuna bo'ldim", callback_data="check"))
    if await functions.check_on_start(message.from_user.id):
        id = message.text
        if message.text.isdigit() == True:
            try:

                send = await message.reply("Iltimos biroz kuting...")
                text = await one_data_get(id)
                await send.delete()
                await message.reply(text[0])
                name = text[1]
                if name == "Ma'lumot topilmadi":
                    pass
                else:
                    # sent = await message.reply("Keyingi ma'lumotlar yuklanmoqda\nIltimos biroz kuting...⌛️")
                    # text = await two_data_get(id)
                    # await sent.delete()
                    await message.reply("Keyingi ma'lumotlar mandat chiqqandan keyin ko'rsatiladi")

            except:
                await message.reply("Sayt bilan aloqa uzilib qoldi, iltimos 3 daqiqadan keyin yana urinib ko'ring yana ko'ring")
        else:
            await message.reply("Abiturent ID sini to'g'ri kiriting")
    else:
        await message.answer("Botimizdan foydalanish uchun kanalimizga azo bo'ling", reply_markup=join_inline)

@dp.callback_query_handler( state=From.natijaS, text="check")
async def check(call: CallbackQuery):
    user_id = call.from_user.id
    if await functions.check_on_start(user_id):
        await call.answer()
        await call.message.delete()
        await dp.bot.copy_message(chat_id=call.from_user.id, from_chat_id=5246872049, message_id=319)
    else:
        await call.answer(show_alert=True, text="Botimizdan foydalanish uchun kanalimizga azo bo'ling")


@dp.message_handler(text="📝Baxolash mezonlari")
async def helper(message: types.Message):
    await message.reply("""<b>Bakalavriat 2022-2023-o'quv yili uchun baholash mezonlari!</b>

Joriy yilda ham testda maksimal ball 189 bo‘ladi

<b>👉 Barcha test topshiruvchilar uchun majburiy bo‘lgan 3 ta fan bo‘yicha:</b>

<b>Ona tili </b>(o‘zbek, rus yoki qoraqalpoq tili) - 10 ta savol.
Har biri uchun 1,1 balldan.
Maksimal ball – 11 ball.

<b>Matematika </b>- 10 ta savol.
Har biri uchun 1,1 balldan.
Maksimal ball – 11 ball.

<b>O‘zbekiston tarixi</b> - 10 ta savol.
Har biri uchun 1,1 balldan.
Maksimal ball – 11 ball.

<b>Jami to‘plash mumkin bo‘lgan ball</b> – 33 ball.


<b>👉 Bakalavriat ta’lim yo‘nalishiga mos bo‘lgan 2 ta fan bo‘yicha:</b>

<b>1-fan - 30 ta savol.</b>
Har biri uchun 3,1 balldan.
Maksimal ball – 93 ball.

<b>2-fan - 30 ta savol.</b>
Har biri uchun 2,1 balldan.
Maksimal ball – 63 ball.

Jami to‘plash mumkin bo‘lgan ball – 156 ball.

Umumiy holda, 2022-2023 o‘quv yili qabulida abituriyentlarga 5 ta fan bo‘yicha jami 90 ta test topshirig‘i beriladi. Bunda to‘plash mumkin bo‘lgan maksimal ball – 189 ballni tashkil etadi.

<b>Ta’lim tizimiga oid yangiliklar: 
➡️ @Xorijdan_Perevod
➡️ @MandatNatijalari_bot</b>""")


@dp.message_handler(commands='stop')
async def helper(message: types.Message):
    await message.reply("Orqaga qaytildi", reply_markup=frond_btn)


# O'qishni ko'chirish                  '''''''''''''''''''


@dp.message_handler(text="📘O'qishni ko'chirish️")
async def helper(message: types.Message):
    sql.execute("SELECT id FROM channels")
    rows = sql.fetchall()
    join_inline = types.InlineKeyboardMarkup(row_width=1)
    title = 1
    for row in rows:
        all_details = await dp.bot.get_chat(chat_id=row[0])
        url = all_details['invite_link']
        join_inline.insert(InlineKeyboardButton(f"{title} - kanal", url=url))
        title += 1
    join_inline.add(InlineKeyboardButton("✅Obuna bo'ldim", callback_data="check"))
    if await functions.check_on_start(message.from_user.id):
        await message.reply("Tanlang👇", reply_markup=transfer_btn)
    else:
        await message.answer("Botimizdan foydalanish uchun kanalimizga azo bo'ling", reply_markup=join_inline)


#

@dp.message_handler(text="〽Natija️")
async def helper(message: types.Message):

    await message.reply("<b>Abituriyent ID raqamini yuboring va imtihon natijalaringiz bilan tanishing!</b>",
                        reply_markup=orqagaBtn)
    await dp.bot.copy_message(chat_id=message.from_user.id, from_chat_id=5246872049, message_id=319)
    await From.natija2S.set()


@dp.message_handler(state=From.natija2S, text="⏪Orqaga qaytish")
async def helper(message: types.Message, state: FSMContext):
    await message.reply("Orqaga qaytildi", reply_markup=transfer_btn)
    await state.finish()


@dp.message_handler(state=From.natija2S, commands='stop')
async def helper(message: types.Message, state: FSMContext):
    await message.reply("Orqaga qaytildi", reply_markup=transfer_btn)
    await state.finish()


@dp.message_handler(state=From.natija2S, content_types=types.ContentType.TEXT)
async def f(message: types.Message):
    sql.execute("SELECT id FROM channels")
    rows = sql.fetchall()
    join_inline = types.InlineKeyboardMarkup(row_width=1)
    title = 1
    for row in rows:
        all_details = await dp.bot.get_chat(chat_id=row[0])
        url = all_details['invite_link']
        join_inline.insert(InlineKeyboardButton(f"{title} - kanal", url=url))
        title += 1
    join_inline.add(InlineKeyboardButton("✅Obuna bo'ldim", callback_data="check"))
    if await functions.check_on_start(message.chat.id):
        id = message.text
        if message.text.isdigit() == True:
            try:

                send = await message.reply("Iltimos biroz kuting...")
                text = await get_data(id)
                await send.delete()
                await message.reply(f"{text[0]}\n{text[1]}\n\n@MandatNatijalari_bot")

            except:
                await message.reply("ID bo'yicha ma'lumot topilmadi")
        else:
            await message.reply("Abiturent ID sini to'g'ri kiriting")
    else:
        await message.answer("Botimizdan foydalanish uchun kanalimizga azo bo'ling", reply_markup=join_inline)

@dp.callback_query_handler( state=From.natija2S, text="check")
async def check(call: CallbackQuery):
    user_id = call.from_user.id
    if await functions.check_on_start(user_id):
        await call.answer()
        await call.message.delete()
        await dp.bot.copy_message(chat_id=call.from_user.id, from_chat_id=5246872049, message_id=319)
    else:
        await call.answer(show_alert=True, text="Botimizdan foydalanish uchun kanalimizga azo bo'ling")

#####################################################

@dp.message_handler(text="📝Baxolash mezonlari️")
async def helper(message: types.Message):
    print(message.message_id)
    await dp.bot.copy_message(chat_id=message.from_user.id, from_chat_id=5246872049, message_id=323)



@dp.message_handler(text="💰Super kontrakt miqdori️")
async def helper(message: types.Message):
    await dp.bot.copy_message(chat_id=message.from_user.id, from_chat_id=5246872049, message_id=322)


@dp.message_handler(content_types="any")
async def helper(message: types.Message):
    await message.reply("Boshidan keting", reply_markup=frond_btn)


if __name__ == "__main__":
    executor.start_polling(dp)
