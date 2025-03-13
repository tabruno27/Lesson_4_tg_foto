import os
import requests


def download_image(url, save_folder, filename):
    img_response = requests.get(url)
    img_response.raise_for_status()
    file_path = os.path.join(save_folder, filename)
    with open(file_path, 'wb') as file:
        file.write(img_response.content)
    return file_path

def get_image_folder():
    return "images"

if __name__ == "__main__":
    image_folder = get_image_folder()
    os.makedirs(image_folder, exist_ok=True)

