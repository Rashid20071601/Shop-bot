from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from texts import texts
from logging_config import setup_logger

# Настраиваем логгер
logger = setup_logger()

# Логируем начало создания клавиатур
logger.info("Создание reply-клавиатур...")

# Клавиатура для работы с данными пользователя
user_data_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=texts.update_data), KeyboardButton(text=texts.delete_data)],
    ], resize_keyboard=True, one_time_keyboard=True
)
logger.debug("Создана reply-клавиатура для работы с данными пользователя: user_data_kb")

# Клавиатура для стартового меню
start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=texts.cart), KeyboardButton(text=texts.catalog)],
        [KeyboardButton(text=texts.change_data)],
    ], resize_keyboard=True, one_time_keyboard=True
)
logger.debug("Создана стартовая reply-клавиатура: start_kb")

# Клавиатура для корзины
cart_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=texts.delete_product_from_cart), KeyboardButton(text=texts.clear_cart)],
    ], resize_keyboard=True, one_time_keyboard=True
)
logger.debug("Создана reply-клавиатура для корзины: cart_kb")

# Клавиатура для всех команд
commands_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=texts.update_data), KeyboardButton(text=texts.delete_data)],
        [KeyboardButton(text=texts.cart), KeyboardButton(text=texts.catalog)],
        [KeyboardButton(text=texts.delete_product_from_cart), KeyboardButton(text=texts.clear_cart)],
    ], resize_keyboard=True, one_time_keyboard=True
)
logger.debug("Создана reply-клавиатура для всех команд: commands_kb")

# Логируем завершение создания клавиатур
logger.info("Reply-клавиатуры успешно созданы.")