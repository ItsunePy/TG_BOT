import telebot as tb

joke = tb.types.KeyboardButton('Анекдот')
tost = tb.types.KeyboardButton('Тост')
aforism = tb.types.KeyboardButton('Афоризм')
cat = tb.types.KeyboardButton('Котик')
fox = tb.types.KeyboardButton('Лисичка')

imgs = tb.types.KeyboardButton('Случайные картинки')
fun = tb.types.KeyboardButton('Развлечения')
back = tb.types.KeyboardButton('Назад')

imgs_markup = tb.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
imgs_markup.add(cat, fox, back)

fun_markup = tb.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
fun_markup.add(joke, tost, aforism, back)