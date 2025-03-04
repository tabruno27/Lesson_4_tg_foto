import argparse
import requests
import utils
from utils import create_image_folder, download_image


def fetch_spacex_images(launch_id=None):
    """Получает изображения SpaceX по ID запуска и скачивает их."""
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}" if launch_id else "https://api.spacexdata.com/v5/launches/latest"
    response = requests.get(url)

    if response.status_code == 200:
        launch_data = response.json()
        image = launch_data.get('links', {}).get('flickr', {}).get('original')

        image_folder = utils.image_folder
        create_image_folder(image_folder)

        for index, img_url in enumerate(image, start=1):
            download_image(img_url, image_folder, f"spacex{index + 1}.jpg")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скачать изображения SpaceX по ID запуска.")
    parser.add_argument("--launch_id", type=str, help="ID запуска SpaceX")
    args = parser.parse_args()

    fetch_spacex_images(args.launch_id)
