import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlsplit, unquote
from os.path import splitext
import utils
from utils import create_image_folder, download_image


def get_file_extension(url):
    """Получает расширение файла из URL."""
    path = urlsplit(url).path
    filename = os.path.basename(unquote(path))
    _, extension = splitext(filename)
    return extension


def fetch_apod_images(count=30):
    """Получает несколько изображений из NASA APOD и сохраняет их с правильными расширениями."""
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&count={count}"
    response = requests.get(url)

    if response.status_code == 200:
        apod_data = response.json()

        # Создаем директорию для изображений, если она не существует
        image_folder = utils.image_folder
        create_image_folder(image_folder)  # Используем функцию для создания папки

        for index, item in enumerate(apod_data):
            img_url = item.get('url')
            if img_url:
                # Получаем расширение файла
                file_extension = get_file_extension(img_url)
                # filename = os.path.join(image_folder, f"apod_image_{index + 1}{file_extension}")  # Формируем имя файла

                # Скачиваем изображение с помощью функции download_image
                try:
                    download_image(img_url, image_folder, f"apod_image_{index + 1}{file_extension}")  # Передаем папку для сохранения
                    # print(f"Изображение сохранено как: {filename}")
                except Exception as e:
                    print(f"Ошибка при скачивании изображения {img_url}: {e}")
            else:
                print("Изображение не найдено в ответе APOD.")

    else:
        print(f"Ошибка: {response.status_code}")


if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv('NASA_API_KEY')

    fetch_apod_images(count=30)
