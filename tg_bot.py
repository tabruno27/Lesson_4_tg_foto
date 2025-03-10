import os
import random
import time
import telegram
import argparse
from dotenv import load_dotenv
import utils


def get_photos_from_directory(directory):
    if not os.path.exists(directory):
        print(f"Директория {directory} не найдена.")
        return []

    return [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg'))]


def shuffle_photos(photos):
    random.shuffle(photos)
    return photos


def publish_photos(directory, publish_interval, bot, chat_id):
    photos = get_photos_from_directory(directory)
    if not photos:
        print("Нет фотографий для публикации.")
        return

    while True:
        shuffled_photos = shuffle_photos(photos) 
        for photo in shuffled_photos:
            photo_path = os.path.join(directory, photo)
            publish_photo(bot, chat_id, photo_path) 
            time.sleep(publish_interval)


if __name__ == "__main__":
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('CHAT_ID')

    parser = argparse.ArgumentParser(description='Публикация фотографий в Telegram.')
    parser.add_argument('--interval', type=int, default=14400,
                        help='Интервал публикации в секундах (по умолчанию 4 часа)')
    parser.add_argument('--photo', type=str,
                        help='Имя фотографии для публикации (если не указано, публикуется случайная фотография)')

    args = parser.parse_args()
    bot = telegram.Bot(token=tg_token)

    directory = utils.image_folder
    publish_photos(directory, args.interval)
