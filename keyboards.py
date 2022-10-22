from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button2 = InlineKeyboardButton(text="🕹️Игры", callback_data="button2")
button3 = InlineKeyboardButton(text="⛔Рынок", callback_data="button3")
button4 = InlineKeyboardButton(text="❣️Развлекательные", callback_data="button4")
button1 = InlineKeyboardButton(text="🤟Основные", callback_data="button1")
button5 = InlineKeyboardButton(text="⚔️Модерация", callback_data="button5")
button6 = InlineKeyboardButton(text="💥Имущества", callback_data="button6")
button7 = InlineKeyboardButton(text="💳Заработок", callback_data="button7")
button8 = InlineKeyboardButton(text="💻Соц.Сети", callback_data="button8")
button9 = InlineKeyboardButton(text="Добавить бота в чат👹", url="https://t.me/varzay_bot?startgroup=true")


kk = InlineKeyboardMarkup()
kk.row(button1, button4)
kk.row(button2, button3)
kk.row(button5, button6)
kk.row(button7, button8)
kk.row(button9)




button10 = InlineKeyboardButton(text="Добавить бота в чат👹", url="https://t.me/varzay_bot?startgroup=true")
nk2 = InlineKeyboardMarkup().add(button10)


kit_b1 = InlineKeyboardButton(text="  💚ВИП  ", callback_data="kit_b1")
kit_b2 = InlineKeyboardButton(text="  💙ЛЕГЕНДА  ", callback_data="kit_b2")
kit_b3 = InlineKeyboardButton(text="  💜СПОНСОР  ", callback_data="kit_b3")
kit_b4 = InlineKeyboardButton(text="  🖤ВЛАСТЕЛИН  ", callback_data="kit_b4")
kit_kb = InlineKeyboardMarkup()
kit_kb = (kit_b1, kit_b2)
kit_kb = (kit_b3, kit_b4)

don1 = InlineKeyboardButton(text="   📝Привилегии   ", callback_data="don1")
don2 = InlineKeyboardButton(text="   🆘Администрация   ", callback_data="don2")
don = InlineKeyboardMarkup().add(don1, don2)

game1 = InlineKeyboardButton(text="🕹️Играть", callback_data="game1")
gm = InlineKeyboardMarkup().add(game1)


