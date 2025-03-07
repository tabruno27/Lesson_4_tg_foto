import argparse
import requests
import utils
from utils import create_image_folder, download_image


def fetch_spacex_images(launch_id=None):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}" if launch_id else "https://api.spacexdata.com/v5/launches/latest"
    response = requests.get(url)

   if not response.ok:
        print(f"Ошибка при получении данных: {response.status_code}")
        return
       
    image_data = response.json()
    image = launch_data.get('links', {}).get('flickr', {}).get('original')

     if not images:
        print("Изображения не найдены для данного запуска.")
        return
        
        image_folder = utils.image_folder
        
        for index, img_url in enumerate(images, start=1):
        try:
            download_image(img_url, image_folder, f"spacex_{index}.jpg")
        except Exception as e:
            print(f"Ошибка при скачивании изображения {img_url}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скачать изображения SpaceX по ID запуска.")
    parser.add_argument("--launch_id", type=str, help="ID запуска SpaceX")
    args = parser.parse_args()

    fetch_spacex_images(args.launch_id)
