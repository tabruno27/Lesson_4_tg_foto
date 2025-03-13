import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlsplit, unquote
from os.path import splitext
from utils import download_image, get_image_folder


def get_file_extension(url):
    path = urlsplit(url).path
    filename = os.path.basename(unquote(path))
    _, extension = splitext(filename)
    return extension


def fetch_apod_images(nasa_api_key, count=30):
    url = f"https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params={
        "api_key": nasa_api_key,
        "count": count
    })

    if not response.ok:
        print(f"Ошибка: {response.status_code}")
        return

    apod_image_data = response.json()
    image_folder = get_image_folder()

    for index, image in enumerate(apod_image_data, start=1):
        img_url = image.get('url')
        if not img_url:
            print("Изображение не найдено в ответе APOD.")
            continue

        file_extension = get_file_extension(img_url)

        try:
            download_image(img_url, image_folder, f"apod_image_{index}{file_extension}")
        except (requests.HTTPError, requests.ConnectionError) as e:
            print(f"Ошибка при скачивании изображения {img_url}: {e}")


def main():
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')

    fetch_apod_images(nasa_api_key, count=30)

if __name__ == "__main__":
    main()
