from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from logging_config import setup_logger

# Настраиваем логгер
logger = setup_logger()

# Логируем начало создания клавиатур
logger.info("Создание клавиатур...")

# Клавиатура для удаления данных
delete_data_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅ Да, удалить', callback_data='yes'),
         InlineKeyboardButton(text='❌ Нет, оставить', callback_data='no')],
    ]
)
logger.debug("Создана клавиатура для удаления данных: delete_data_kb")

# Клавиатура для возврата
back_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🔙 Вернуться назад', callback_data='back')],
    ]
)
logger.debug("Создана клавиатура для возврата: back_kb")

# Клавиатура для корзины
def cart_kb(product_id: int):
    logger.debug(f"Создана клавиатура для корзины с product_id={product_id}")
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🔙 Вернуться назад', callback_data='back')],
            [InlineKeyboardButton(text='🛒 Добавить в корзину', callback_data=f'cart_{product_id}')]
        ]
    )

# Клавиатура для очистки корзины
ask_clear_cart_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🧹 Да, очистить корзину', callback_data='confirm_clear_cart')],
        [InlineKeyboardButton(text='❌ Нет, оставить товары', callback_data='cancel_clear_cart')]
    ]
)
logger.debug("Создана клавиатура для очистки корзины: ask_clear_cart_kb")

# Логируем завершение создания клавиатур
logger.info("Клавиатуры успешно созданы.")