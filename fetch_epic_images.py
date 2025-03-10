import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import argparse
import utils
from utils import download_image


def fetch_epic_images(api_key, date_str=None, count=None):
    start_date = datetime.strptime(args.date, "%Y-%m-%d")
    dates = [start_date + timedelta(days=i) for i in range(args.count)]
    
    

    for date in dates:
        date_str = date.strftime("%Y-%m-%d")
        url = f"https://api.nasa.gov/EPIC/api/natural/date/{date_str}?{query_string}"
        response = requests.get(url, params={ 
             'api_key': api_key,
        })

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"Ошибка при запросе: {err}")
            continue

        image_data = response.json()
        if not launch_data:
            print(f"Нет данных для даты: {date_str}")
            continue

        image_folder = utils.image_folder

        for index, image_data in enumerate(launch_data):
            image_name = image_data['image']
            img_url = f"https://api.nasa.gov/EPIC/archive/natural/{date.year}/{date.month:02}/{date.day:02}/png/{image_name}.png?{query_string}"

            download_image(img_url, image_folder, f"image_{date_str}_{index + 1}.png")

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
