import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlsplit, unquote
from os.path import splitext
import utils
from utils import download_image


def get_file_extension(url):
    path = urlsplit(url).path
    filename = os.path.basename(unquote(path))
    _, extension = splitext(filename)
    return extension


def fetch_apod_images(api_key, count=None):

    url = f"https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params={
        "api_key": api_key,
        'count": count
    })

    if not response.ok:
        print(f"Ошибка: {response.status_code}")
        return

    image_data = response.json()
    image_folder = utils.image_folder

    for index, item in enumerate(apod_data):
        img_url = item.get('url')
        if not img_url:
            print("Изображение не найдено в ответе APOD.")
            continue 

        file_extension = get_file_extension(img_url)

         try:
            download_image(img_url, image_folder, f"apod_image_{index + 1}{file_extension}")
        except (requests.HTTPError, requests.ConnectionError) as e:
            print(f"Ошибка при скачивании изображения {img_url}: {e}")
        except FileNotFoundError as e:
            print(f"Ошибка: не удалось найти файл для сохранения изображения: {e}")
            

def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')

    fetch_apod_images(count=30, api_key)

if __name__ == "__main__":
    main()
