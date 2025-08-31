# Импорт библиотек
import logging
from aiogram import types
from . import catalog, start, cart
from texts import texts
from aiogram.dispatcher.storage import FSMContext
from logging_config import setup_logger

# Настроим логгер
logger = setup_logger()

async def back_button_handler(call: types.CallbackQuery, state: FSMContext):
    # Получаем данные состояния
    state_data = await state.get_data()

    # Логируем получение данных состояния
    logger.info(f"Получены данные состояния: {state_data}")

    # Проверяем, на каком шаге находится пользователь
    current_step = state_data.get('current_step')
    selected_category = state_data.get('selected_category')

    # Логируем текущий шаг и выбранную категорию
    logger.info(f"Текущий шаг: {current_step}, Выбранная категория: {selected_category}")

    if not current_step:   # Если не удалось получить шаг (что-то пошло не так)
        logger.warning("Не удалось получить текущий шаг, ошибка.")
        await call.message.answer(texts.back_error)
        return

    # ========================= START ========================= #
    # Если пользователь на начальном этапе, просто отменяем команду
    if current_step == 'start':
        logger.info("Пользователь на начальном шаге, выводим текст.")
        await call.message.answer(texts.back_if_start)

    elif current_step == 'help' or current_step == 'commands' or current_step == 'cart':
        logger.info(f"Переход от этапа '{current_step}' к этапу 'start'.")
        await state.update_data(current_step='start')
        await start.send_start(call.message, state)


    # ========================= CATALOG ========================= #
    # Возвращаем пользователя на предыдущий этап
    elif current_step == 'product_details':
        logger.info(f"Переход от этапа 'product_details' к этапу 'product'.")
        await state.update_data(current_step='product')  # Назад к списку товаров
        await catalog.show_products_by_category(call.message, state, category=selected_category)
    
    elif current_step == 'product':
        logger.info(f"Переход от этапа 'product' к этапу 'category'.")
        await state.update_data(current_step='category')  # Назад к категориям
        await catalog.show_categories(call.message, state=state)  # Возвращаем к списку категорий

    elif current_step == 'category':
        logger.info(f"Переход от этапа 'category' к этапу 'start'.")
        await state.update_data(current_step='start')
        await start.send_start(call.message, state)


    # ========================= SHOPPING CART ========================= #
    elif current_step == 'add_to_cart':
        logger.info(f"Переход от этапа 'add_to_cart' к этапу 'cart'.")
        await state.update_data(current_step='cart')
        await cart.view_cart(call.message, state)


    # ========================= ERROR ========================= #
    else:
        logger.error(f"Неизвестный шаг: {current_step}. Выводим ошибку.")
        await call.message.answer(texts.back_error)
    
    await call.answer()
