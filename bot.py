import telebot
from telebot import types

# Замени 'ВАШ_ТОКЕН_БОТА' на токен, который ты получил у @BotFather
bot = telebot.TeleBot('8304482760:AAFAEMy36geI_qZMxKxSFgSFx9KsPaT7AKc')

@bot.message_handler(commands=['start'])
def start(message):
    # Создаем объект клавиатуры
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Создаем кнопку Mini App
    # ВАЖНО: Твоя ссылка https://yourdestiny.hgweb.ru
    web_app = types.WebAppInfo("https://yourdestiny.hgweb.ru")
    
    # Текст на кнопке, которая открывает сайт прямо внутри Telegram
    btn = types.KeyboardButton(text="✨ Узнать свою судьбу 2026", web_app=web_app)
    
    markup.add(btn)
    
    # Приветственный текст
    welcome_text = (
        f"Привет, {message.from_user.first_name}! ✨\n\n"
        "Твой 2026 год уже предначертан. Мы подготовили для тебя персональный прогноз "
        "на основе твоей цифровой энергии.\n\n"
        "Нажми на кнопку ниже, чтобы открыть Mini App и узнать свою судьбу! 👇"
    )
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен и готов предсказывать будущее...")
    bot.polling(none_stop=True)
