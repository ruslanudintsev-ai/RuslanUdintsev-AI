import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Получение токена из переменных окружения
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет приветственное сообщение с кнопками."""
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("ℹ️ О боте", callback_data="about")],
        [InlineKeyboardButton("📋 Список команд", callback_data="commands")],
        [InlineKeyboardButton("🎲 Тестовая кнопка", callback_data="test")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"👋 Привет, {user.first_name}!\n\n"
        f"Я интерактивный демонстрационный бот.\n"
        f"Выберите опцию ниже:",
        reply_markup=reply_markup,
    )


# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет справку по командам."""
    help_text = (
        "📚 **Список доступных команд:**\n\n"
        "/start - Запустить бота и показать главное меню\n"
        "/help - Показать эту справку\n"
        "/echo <текст> - Повторить ваш текст\n"
        "/info - Показать информацию о вас\n"
        "\n"
        "Также вы можете нажимать на кнопки в главном меню!"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")


# Обработчик команды /echo
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Повторяет текст пользователя."""
    if context.args:
        text = " ".join(context.args)
        await update.message.reply_text(f"🔊 Вы сказали: {text}")
    else:
        await update.message.reply_text("⚠️ Пожалуйста, введите текст после команды /echo")


# Обработчик команды /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показывает информацию о пользователе."""
    user = update.effective_user
    chat = update.effective_chat
    
    info_text = (
        f"👤 **Информация о пользователе:**\n\n"
        f"ID: `{user.id}`\n"
        f"Имя: {user.first_name}"
    )
    if user.last_name:
        info_text += f"\nФамилия: {user.last_name}"
    if user.username:
        info_text += f"\nЮзернейм: @{user.username}"
    
    info_text += f"\n\n💬 **Информация о чате:**\n"
    info_text += f"ID чата: `{chat.id}`\n"
    info_text += f"Тип: {chat.type}"
    
    await update.message.reply_text(info_text, parse_mode="Markdown")


# Обработчик нажатий на кнопки
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает нажатия на инлайн-кнопки."""
    query = update.callback_query
    await query.answer()  # Подтверждение получения нажатия
    
    if query.data == "about":
        about_text = (
            "🤖 **О боте**\n\n"
            "Этот бот создан для демонстрации возможностей:\n"
            "• Работа с командами\n"
            "• Инлайн-кнопки\n"
            "• Обработка текстовых сообщений\n"
            "• Интерактивные элементы\n\n"
            "Создан с использованием python-telegram-bot v21.0"
        )
        await query.edit_message_text(about_text, parse_mode="Markdown")
        
    elif query.data == "commands":
        commands_text = (
            "📋 **Доступные команды:**\n\n"
            "/start - Главное меню\n"
            "/help - Справка\n"
            "/echo - Повтор текста\n"
            "/info - Информация о пользователе"
        )
        await query.edit_message_text(commands_text, parse_mode="Markdown")
        
    elif query.data == "test":
        keyboard = [
            [InlineKeyboardButton("✅ Да", callback_data="yes")],
            [InlineKeyboardButton("❌ Нет", callback_data="no")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🎲 Тестовое взаимодействие!\nВы уверены?",
            reply_markup=reply_markup,
        )
        
    elif query.data == "yes":
        await query.edit_message_text("✅ Отлично! Вы выбрали 'Да'")
        
    elif query.data == "no":
        await query.edit_message_text("❌ Хорошо! Вы выбрали 'Нет'")


# Обработчик обычных сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает обычные текстовые сообщения."""
    text = update.message.text
    await update.message.reply_text(
        f"💬 Я получил ваше сообщение: '{text}'\n\n"
        f"Используйте /help для списка команд."
    )


# Обработчик ошибок
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Логирует ошибки."""
    logger.warning(f"Update {update} caused error {context.error}")


def main():
    """Запуск бота."""
    if not TOKEN:
        logger.error("❌ Токен бота не найден! Установите TELEGRAM_BOT_TOKEN в .env файле")
        return
    
    # Создание приложения
    application = Application.builder().token(TOKEN).build()
    
    # Регистрация обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("echo", echo))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Регистрация обработчика ошибок
    application.add_error_handler(error_handler)
    
    # Запуск поллинга
    logger.info("🚀 Бот запускается...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
