# API для магазина проката DVD 

## Описание
В проекте реализован апи бизнес процесса для магазина видеопроката.
Базу данных можно взять [здесь](https://neon.tech/postgresql/postgresql-getting-started/postgresql-sample-database),
там же инструкция как развернуть её локально

## Установка
Для работы проекта потребуется установленный Python 3.12
- склонировать проект локально
- для установки необходимых зависимостей выполнить `pip install -r requirements.txt` 

## Запуск
Находясь в папке с проектом выполнить:
`py app.py` 

Запустится Uvicorn-сервер по дефолтному адресу(указан в консоли или в файле app.py)
url методов можно посмотреть в файле или по адресу сервера + docs#(дефолтно http://127.0.0.1:5000/docs#/)

Для остановки сервера нажать Ctrl+C в терминале

## Сценарий

- /fake-auth для получения айди сотрудника и магазина,в котором сотрудник закреплен
- /film для выбора фильма, /film/in-store для выбора фильмов в наличии в магазине
- /check-in-store для проверки наличия фильма в магазине(если искали по всем фильмам)
- /customer для получения id покупателя(нужен для дальнейших операций)
- /payment для проведения оплаты
- /rent для записи факта проката


## Ряд допущений

### fake-auth?
Метод возвращает айди сотрудника в теле ответа,в обычном процессе это должен быть  jwt-токен который в дальнейшем используется в запросе

### если пришел новый покупатель?
Метода для создания нового покупателя не реализован, только существующий, список отраженный в БД

### есть ли проверки в операции оплаты?
Нет, метод передает сумму оплаты,которая на прямую записывается. Считается что стоимость взята из стоимости аренды фильма(поле в таблице) и погашена полностью, без минуса или плюса.


