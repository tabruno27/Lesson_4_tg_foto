import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import argparse
from utils import download_image, get_image_folder


def fetch_epic_images(api_key, start_date_str, count):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    dates = [start_date + timedelta(days=i) for i in range(count)]

    for date in dates:
        date_str = date.strftime("%Y-%m-%d")
        url = f"https://api.nasa.gov/EPIC/api/natural/date"
        response = requests.get(url, params={
            "api_key": api_key,
            "date": date_str,
        })

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"Ошибка при запросе: {err}")
            continue

        epic_image_data = response.json()
        if not epic_image_data:
            print(f"Нет данных для даты: {date_str}")
            continue

        image_folder = get_image_folder()

        for index, image_data in enumerate(epic_image_data, start=1):
            image_name = image_data['image']
            img_url = f"https://api.nasa.gov/EPIC/archive/natural/{date.year}/{date.month:02}/{date.day:02}/png/{image_name}.png"
            download_image(img_url, image_folder, f"image_{date_str}_{index}.png")


def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    parser = argparse.ArgumentParser(description='Загрузите EPIC-фото NASA.')
    parser.add_argument('--date', type=str, required=True,
                        help='Дата в формате YYYY-MM-DD (обязательно)')
    parser.add_argument('--count', type=int, default=5,
                        help='Количество дней для загрузки изображений (по умолчанию 5)')
    args = parser.parse_args()

    fetch_epic_images(api_key, args.date, args.count)

if __name__ == "__main__":
    main()
