# Импорт библиотек
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import config
from texts import texts
from logging_config import setup_logger
import handlers.back
import handlers.cart
import handlers.catalog
import handlers.data
import handlers.start
from dotenv import load_dotenv
import os
import asyncio


# --------------- Настрройка токена --------------- #
# Загружаем переменные из .env
load_dotenv()

# Получаем токен из окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверяем, что токен загружен
if not BOT_TOKEN:
    raise ValueError("Токен бота не найден! Проверь .env файл.")


# --------------- Настройка логирования --------------- #
# Настраиваем логгер
logger = setup_logger()

# Логируем запуск бота
logger.info("Бот запущен!")


# --------------- Инициализация бота и диспетчера --------------- #
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

EXCLUDED_BUTTONS = [
    texts.cart,
    texts.delete_product_from_cart,
    texts.clear_cart,
    texts.catalog,
    texts.update_data,
    texts.delete_data,
    texts.change_data,
    ]


async def main():
    await dp.start_polling(bot)


# ==================== Регистрация обработчиков команд ====================

# Обработчик команды /start
dp.message(Command('start'))(handlers.start.send_welcome)
logger.info("Обработчик команды /start зарегистрирован")

# Обработчик команды /help
dp.message(Command('help'))(handlers.start.send_help)
logger.info("Обработчик команды /help зарегистрирован")

# Обработчик команды /commands
dp.message(Command('commands'))(handlers.start.show_commands)
logger.info("Обработчик команды /commands зарегистрирован")

# Обработчик нажатия кнопки "Назад"
dp.callback_query(lambda call: call.data == 'back')(handlers.back.back_button_handler)
logger.info("Обработчик кнопки 'Назад' зарегистрирован")


# ==================== Регистрация обработчиков категорий и товаров ====================

# Обработчик команды /catalog для отображения категорий
dp.message(lambda message: message.text == texts.catalog)(handlers.catalog.show_categories)
logger.info("Обработчик команды /catalog зарегистрирован")

# Обработчик выбора категории
dp.message(lambda message: message.text and not message.text.isdigit() and message.text not in EXCLUDED_BUTTONS)(handlers.catalog.show_products_by_category_wrapper)
logger.info("Обработчик выбора категории зарегистрирован")

# Обработчик выбора товара
dp.message(lambda message: message.text.isdigit())(handlers.catalog.show_product_details_wrapper)
logger.info("Обработчик выбора товара зарегистрирован")


# ==================== Регистрация обработчиков данных ====================

# Обработчик команды /update
dp.message(lambda message: message.text == texts.change_data)(handlers.data.send_update)
logger.info("Обработчик команды /update зарегистрирован")

# Обработчик для обновления данных
dp.message(lambda message: message.text == texts.update_data)(handlers.data.update_data)
logger.info("Обработчик обновления данных зарегистрирован")

# Обработчик для удаления данных
dp.message(lambda message: message.text == texts.delete_data)(handlers.data.delete_data)
logger.info("Обработчик удаления данных зарегистрирован")

# Обработчик выбора действия (подтверждение удаления)
dp.callback_query(lambda call: call.data in ['yes', 'no'])(handlers.data.choice_delete)
logger.info("Обработчик выбора действия (подтверждение удаления) зарегистрирован")

# Обработчик для получения e-mail
dp.message(config.UserRegistration.waiting_for_email)(handlers.data.get_email)
logger.info("Обработчик получения e-mail зарегистрирован")

# Обработчик для получения телефона
dp.message(config.UserRegistration.waiting_for_phone)(handlers.data.get_phone)
logger.info("Обработчик получения телефона зарегистрирован")


# ==================== Регистрация обработчиков корзины ====================

# Обработчик просмотра товаров в корзине
dp.message(lambda message: message.text == texts.cart)(handlers.cart.view_cart)
logger.info("Обработчик просмотра товаров в корзине зарегистрирован")

# Обработчик для добавления товара в корзину
dp.callback_query(lambda call: call.data.startswith('cart_'))(handlers.cart.add_to_cart)
logger.info("Обработчик добавления товара в корзину зарегистрирован")

# Обработчик удаления товаров в корзине
dp.message(lambda message: message.text == texts.delete_product_from_cart)(handlers.cart.start_remove_from_cart)
dp.message(config.CartState.waiting_for_product_id)(handlers.cart.process_remove_from_cart)
logger.info("Обработчик удаления товаров из корзины зарегистрирован")

# Обработчик очистки корзины
dp.message(lambda message: message.text == texts.clear_cart)(handlers.cart.ask_clear_cart)
dp.callback_query(lambda call: call.data == 'confirm_clear_cart')(handlers.cart.clear_cart)
dp.callback_query(lambda call: call.data == 'cancel_clear_cart')(handlers.cart.do_not_clear_cart)
logger.info("Обработчик очистки корзины зарегистрирован")


# ==================== Запуск бота ====================

logger.info("Запуск бота...")
if __name__ == '__main__':
    try:
        asyncio.run(main())
        logger.info("Бот был успешно запущен.")
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
        raise
    finally:
        logger.info("Бот остановлен.")