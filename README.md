# Сервис по загрузке и обработке файлов

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fastapi?style=plastic)

## Содержание
- [Сервис по загрузке и обработке файлов](#сервис-по-загрузке-и-обработке-файлов)
  - [Содержание](#содержание)
  - [Описание](#описание)
  - [Установка](#установка)
  - [Запуск](#запуск)
  - [Эндпоинты](#эндпоинты)
  - [Выполненные требования к системе](#выполненные-требования-к-системе)
      - [Основные](#основные)
      - [Дополнительные](#дополнительные)
  - [Контакты](#контакты)

## Описание
Разработан API сервис, позволяющий загружать файлы на сервер, а затем асинхронно обрабатывать их с использованием Celery.<br>
Использованный стек технологий: Python3, Django, Django_rest_framework, PostgreSQL, Celery, Redis.<br>
В системе реализована искусственная задержка обработки файла в 10 секунд для демонстрации работы Celery.<br>
Демонстрация работы сервиса: 51.250.84.69/api/v1/files

## Установка
```bash
git clone github.com/SGGM/file_loader_and_processor.git
```


## Запуск
```bash
cd file_loader_and_processor/
docker-compose up --build -d
```


## Эндпоинты
1. Для загрузки и сохранения файлов:
```bash
0.0.0.0/api/v1/upload
```

2. Для просмотра списка всех файлов со статусом их обработки:
```bash
0.0.0.0/api/v1/files
```

## Выполненные требования к системе
### Основные
- [x] Реализована модель File со следующими полями:
```txt
{
    "id": IntField,
    "file": FileField,
    "uploaded_at": DateTimeField,
    "processed": BooleanField
}
```
- [x] Реализован сериализатор для модели File.
- [x] Создан API эндпоинт upload/, позволяющий загружать файлы на сервер.
- [x] С использованием Celery реализован механизм асинхронной обработки файла.
- [x] Создан API эндпоинт files/, возвращающий список всех файлов со статусом обработки.

### Дополнительные
- [x] Развертывание проекта происходит при помощи docker и docker-compose.
- [x] Возвращение соответствующих сообщений об ошибках.

## Контакты
Сомов Глеб<br>
1. Mail.ru - gleb_somov@mail.ru<br>
2. Telegram - [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Stole_your_jet)<br>
