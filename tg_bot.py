import os
import random
import time
import telegram
import argparse
from dotenv import load_dotenv
import utils


def get_photos_from_directory(directory):
    """Получает список фотографий из заданной директории."""
    if not os.path.exists(directory):
        print(f"Директория {directory} не найдена.")
        return []

    return [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg'))]


def publish_photos(directory, publish_interval):
    """Публикует фотографии в Telegram с заданным интервалом."""
    photos = get_photos_from_directory(directory)
    if not photos:
        print("Нет фотографий для публикации.")
        return

    while True:
        random.shuffle(photos)  # Перемешиваем список фотографий
        for photo in photos:
            photo_path = os.path.join(directory, photo)
            with open(photo_path, 'rb') as file:
                bot.send_photo(chat_id=CHAT_ID, photo=file)
                print(f"Фото опубликовано: {photo}")
            time.sleep(publish_interval)  # Задержка перед публикацией следующей фотографии


if __name__ == "__main__":
    load_dotenv()
    TG_API = os.getenv('TG_API')
    CHAT_ID = os.getenv('CHAT_ID')

    parser = argparse.ArgumentParser(description='Публикация фотографий в Telegram.')
    parser.add_argument('--interval', type=int, default=14400,
                        help='Интервал публикации в секундах (по умолчанию 4 часа)')
    parser.add_argument('--photo', type=str,
                        help='Имя фотографии для публикации (если не указано, публикуется случайная фотография)')

    args = parser.parse_args()
    bot = telegram.Bot(token=TG_API)

    directory = utils.image_folder
    publish_photos(directory, args.interval)