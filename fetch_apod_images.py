import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('NASA_API_KEY')


def fetch_apod_image():
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        apod_data = response.json()
        img_url = apod_data.get('url')
        img_response = requests.get(img_url)
        filename = img_url.split("/")[-1]
        with open(filename, 'wb') as file:
            file.write(img_response.content)
    else:
        print(f"Ошибка: {response.status_code}")


if __name__ == "__main__":
    fetch_apod_image()