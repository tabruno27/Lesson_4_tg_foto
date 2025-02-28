import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Загружаем переменные окружения
load_dotenv()
API_KEY = os.getenv('NASA_API_KEY')


def get_file_extension(url):
    # Извлекаем расширение из URL
    _, ext = os.path.splitext(url)
    return ext


def fetch_epic_images(start_date, count=5):
    image_folder = "epic_images"
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    # Генерируем даты для загрузки изображений
    dates = [start_date + timedelta(days=i) for i in range(count)]

    for date in dates:
        date_str = date.strftime("%Y-%m-%d")
        url = f"https://api.nasa.gov/EPIC/api/natural/date/{date_str}?api_key={API_KEY}"
        response = requests.get(url, verify=False)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"Ошибка при запросе: {err}")
            continue

        launch_data = response.json()
        if not launch_data:
            print(f"Нет данных для даты: {date_str}")
            continue

        for index, image_data in enumerate(launch_data):
            image_name = image_data['image']
            # Формируем URL для загрузки изображения
            image_url = f"https://api.nasa.gov/EPIC/archive/natural/{date.year}/{date.month:02}/{date.day:02}/png/{image_name}.png?api_key={API_KEY}"

            # Формируем имя файла без параметров URL
            filename = f'image_{date_str}_{index + 1}.png'
            save_path = os.path.join(image_folder, filename)

            # Скачиваем изображение
            try:
                img_response = requests.get(image_url, verify=False)
                img_response.raise_for_status()

                with open(save_path, 'wb') as file:
                    file.write(img_response.content)
                print(f"Скачано: {filename}")
            except requests.exceptions.HTTPError as err:
                print(f"Ошибка при скачивании {image_url}: {err}")


# Пример использования
if __name__ == "__main__":
    # Укажите начальную дату для загрузки изображений
    start_date = datetime.strptime("2025-01-01", "%Y-%m-%d")
    fetch_epic_images(start_date, count=5)
