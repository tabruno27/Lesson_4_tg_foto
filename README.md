# Telegram_bot, который делится фотографиями космоса

![123457](https://github.com/user-attachments/assets/41edc091-746c-425e-bab8-dd5c43b2ca8c)

## Описание

Проект представляет собой набор скриптов на Python, которые позволяют автоматически загружать и публиковать изображения из различных источников, таких как NASA и SpaceX, в Telegram. Он предназначен для любителей космоса и астрономии, которые хотят получать и делиться захватывающими космическими изображениями. Проект использует API NASA и SpaceX для получения изображений и Telegram Bot API для публикации их в чатах.

## Требования

- Python 3.8
Установите необходимые библиотеки с помощью ```pip```:

```bash
pip install -r requirements.txt
```

## Настройка
### Как получить API-ключим

1. **Получите API ключ от NASA**: 
   
   1.1 Перейдите на сайт [NASA API](https://api.nasa.gov).

   1.2 Заполните форму регистрации, указав свои данные, такие как имя, адрес электронной почты и название проекта.

   1.3 После успешной регистрации вы получите свой уникальный API-ключ, который можно использовать в проекте.
   
2. **Получение API-ключа Telegram Bot**:

   2.1 Откройте Telegram и найдите бота [@BotFather](https://telegram.me/BotFather) 

   2.2 Начните диалог с BotFather и используйте команду ```/newbot```.

   2.3 Следуйте инструкциям, чтобы создать нового бота. В конце вы получите токен доступа, который будет выглядеть как строка символов. Сохраните этот токен, он понадобится для работы с Telegram Bot API.

3. **Получение chat_id для канала**:

Чтобы получить ```chat_id``` канала, выполните следующие шаги:

   3.1 Убедитесь, что ваш бот добавлен в канал и имеет права на отправку сообщений.

   3.2 Отправьте любое сообщение в канал.

   3.3 Перейдите по следующей ссылке, заменив ```ваш_токен_бота``` на токен вашего бота:

   ```bash
   https://api.telegram.org/botваш_токен_бота/getUpdates
   ```

   3.4 Найдите в ответе JSON-объекта раздел, который начинается с ```"channel_post"```:. Внутри него будет поле ```"chat"```, содержащее ```"id"```. Это и есть ваш ```chat_id``` канала.

Пример части ответа:

```bash
{
    "update_id": 123456789,
    "channel_post": {
        "message_id": 1,
        "chat": {
            "id": -987654321,
            "title": "Название канала",
            "type": "channel"
        },
        "date": 1610000000,
        "text": "Привет, канал!"
    }
}
```

В данном случае chat_id канала будет равен -987654321.

## Как установить
Перед запуском проекта необходимо установить все зависимости. Для этого выполните следующие шаги:

1. Убедитесь, что у вас установлен Python 3.8. Проверьте это, выполнив команду:

```bash
python --version
```
2. Установите необходимые библиотеки с помощью pip:

```bash
pip install -r requirements.txt
```

3. Создайте файл .env в корневой директории проекта и добавьте следующие переменные:

```bash
TG_TOKEN=ваш_токен_бота
CHAT_ID=ваш_chat_id
NASA_API_KEY=ваш_api_key_nasa
```

Замените значения переменных на ваши собственные.

## Использование

### Загрузка изображений SpaceX

```bash
python fetch_spacex_images.py --launch_id <ваш_launch_id>
```

Если ```launch_id``` не указан, будут загружены изображения последнего запуска.

#### Получение launch_id от SpaceX
Используйте API SpaceX: Вы можете обратиться к API SpaceX, чтобы получить список всех запусков и их идентификаторов. Для этого выполните следующий запрос:

```bash
https://api.spacexdata.com/v4/launches
```

Запрос вернет массив объектов, каждый из которых представляет собой запуск. В каждом объекте будет поле ```id```, которое и является ```launch_id```.

Пример запроса, открыв ссылку в браузере. Вот пример ответа, который вы можете получить:

```bash
[
    {
        "id": "5eb87d0cffd86e000604b386",
        "name": "FalconSat",
        "date_utc": "2022-01-01T00:00:00.000Z",
        "details": "First mission with a Falcon 1 rocket."
        ...
    },
    ...
]
```

В этом примере ```launch_id``` будет равен ```"5eb87d0cffd86e000604b386"```.

### Загрузка изображений NASA EPIC

```bash
python fetch_epic_images.py --date 2025-01-01 --count 5
```

Загрузит изображения NASA EPIC за 5 дней начиная с 1 января 2025 года.

### Загрузка изображений NASA APOD
```bash
python fetch_apod_images.py
```

По умолчанию стоит скачать 30 изображений из NASA APOD. 

После скаченных изображений можно приступить к их публикации в тг боте.

### Запуск скрипта для публикации фотографий в Telegram

```bash
python tg_bot.py --interval 3600
```

Запустит публикацию фотографий с интервалом в 1 час. Вы можете изменить интервал, указав нужное значение в секундах.
По умолчанию стоит 4 часа.

Доп. функции в файле utils.py:
Можно испортировать данные функций из ```utils.py``` в другие свои скрипты.

```bash
from utils import download_image, get_image_folder

# Создание папки для изображений
get_image_folder()

# Скачивание изображения
download_image('https://example.com/image.jpg', 'images', 'image.jpg')
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
