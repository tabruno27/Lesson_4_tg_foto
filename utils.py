import os
import requests


def download_image(url, save_folder, filename):
    img_response = requests.get(url)
    img_response.raise_for_status()
    file_path = os.path.join(save_folder, filename)
    with open(file_path, 'wb') as file:
        file.write(img_response.content)
    return file_path

if __name__ == "__main__":
    image_folder="images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        file_path = download_image(image_url, image_folder, image_filename)
        print(f"Изображение успешно скачано: {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании изображения: {e}")
