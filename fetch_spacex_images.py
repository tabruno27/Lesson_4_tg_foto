import argparse
import requests
from utils import download_image, get_image_folder


def fetch_spacex_images(launch_id='latest'):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)

    if not response.ok:
        print(f"Ошибка при получении данных: {response.status_code}")
        return

    spacex_image_data = response.json()
    images = spacex_image_data.get('links', {}).get('flickr', {}).get('original')

    if not images:
        print("Изображения не найдены для данного запуска.")
        return

    image_folder = get_image_folder()

    for index, img_url in enumerate(images, start=1):
            download_image(img_url, image_folder, f"spacex_{index}.jpg")

def main():
    parser = argparse.ArgumentParser(description="Скачать изображения SpaceX по ID запуска.")
    parser.add_argument("--launch_id", type=str, default='latest',
                        help="ID запуска SpaceX (по умолчанию id последнего запуска SpaceX)")
    args = parser.parse_args()

    fetch_spacex_images(args.launch_id)


if __name__ == "__main__":
    main()
