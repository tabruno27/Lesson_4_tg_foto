# Telegram_bot, который делится фотографиями космоса

## Описание

Этот скрипт на Python загружает изображения, полученные от NASA EPIC (Earth Polychromatic Imaging Camera), для заданной даты и сохраняет их в локальную папку. Он использует API NASA для получения изображений Земли, сделанных из космоса.

## Требования

- Python 3.x
Установите необходимые библиотеки с помощью pip:

```bash
pip install -r requirements.txt
```

## Настройка

1. **Получите API ключ от NASA**: 
   Перейдите на [NASA API](https://api.nasa.gov) и зарегистрируйтесь, чтобы получить свой API ключ.

2. **Создайте файл `.env`**:
   В корневом каталоге проекта создайте файл `.env` и добавьте в него свой API ключ:

   ```plaintext
   NASA_API_KEY=ваш_ключ
   ```

## Использование

1. **Настройте начальную дату**:
   В коде, в разделе `if __name__ == "__main__":`, измените `start_date` на желаемую дату в формате "YYYY-MM-DD".

2. **Запустите скрипт**:
   Выполните скрипт из командной строки:

   ```bash
   python ваш_скрипт.py
   ```

## Функции

### `get_file_extension(url)`

Извлекает расширение файла из заданного URL.

### `fetch_epic_images(start_date, count=5)`

- **start_date**: Дата, с которой начнется загрузка изображений (тип: datetime).
- **count**: Количество дней для загрузки изображений (по умолчанию 5).

Эта функция создает папку `epic_images`, если она не существует, и загружает изображения для заданной даты и последующих дней.

## Пример использования

```python
if __name__ == "__main__":
    start_date = datetime.strptime("2025-01-01", "%Y-%m-%d")
    fetch_epic_images(start_date, count=5)
```

## Примечания

- Убедитесь, что ваш API ключ действителен, иначе вы получите ошибку `API_KEY_INVALID`.
- Скрипт будет игнорировать даты, для которых нет доступных изображений.
