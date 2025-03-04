import os
import requests


image_folder="images"


def create_image_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def download_image(url, save_folder, filename):
    try:
        img_response = requests.get(url)
        img_response.raise_for_status()
        file_path = os.path.join(save_folder, filename)
        with open(file_path, 'wb') as file:
            file.write(img_response.content)
        print(f"Изображение успешно скачано: {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании изображения: {e}")