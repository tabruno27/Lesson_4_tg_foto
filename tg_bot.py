import os
import random
import time
import telegram
import argparse
from dotenv import load_dotenv
from utils import get_image_folder



def get_photos_from_directory(directory):
    if not os.path.exists(directory):
        print(f"Директория {directory} не найдена.")
        return []
    return [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg'))]


def publish_photo(bot, tg_chat_id, photo_path):
    with open(photo_path, 'rb') as file:
        bot.send_photo(tg_chat_id=tg_chat_id, photo=file)
    print(f"Фото опубликовано: {photo_path}")


def publish_photos(photos, directory, publish_interval, bot, tg_chat_id):
    while True:
        random.shuffle(photos)
        for photo in photos:
            photo_path = os.path.join(directory, photo)
            publish_photo(bot, tg_chat_id, photo_path)
            time.sleep(publish_interval)



def main():
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')

    parser = argparse.ArgumentParser(description='Публикация фотографий в Telegram.')
    parser.add_argument('--interval', type=int, default=14400,
                        help='Интервал публикации в секундах (по умолчанию 4 часа)')
    parser.add_argument('--photo', type=str,
                        help='Имя фотографии для публикации (если не указано, публикуется случайная фотография)')

    args = parser.parse_args()
    bot = telegram.Bot(token=tg_token)
    directory = get_image_folder()

    photos = get_photos_from_directory(directory)
    if not photos:
        print("Нет фотографий для публикации.")
        return

    publish_photos(photos, directory, args.interval, bot, tg_chat_id)


if __name__ == "__main__":
    main()
