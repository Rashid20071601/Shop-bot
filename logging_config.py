import logging

# Настройка логирования
def setup_logger():

    # Настраиваем логирование в файл
    logging.basicConfig(
        filename='bot.log', 
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8',
        filemode='w'
    )

    # Создаём логгер
    logger = logging.getLogger()
    return logger