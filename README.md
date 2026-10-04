# Environment Configuration Demo

Небольшой Python-проект, демонстрирующий работу с переменными окружения через файл `.env` и библиотеку `python-dotenv`.

Программа загружает настройки из файла конфигурации, проверяет наличие обязательных переменных и безопасно сообщает, был ли загружен секретный ключ, не выводя его значение.

## Требования

- Python 3.10+
- Git

## Установка

### 1. Клонирование репозитория

```powershell
git clone https://github.com/Polina-Soboleva/git_project
cd git_project
```

### 2. Создание виртуального окружения

```powershell
python -m venv .venv
```

### 3. Активация виртуального окружения

```powershell
.\.venv\Scripts\Activate.ps1
```

После активации в начале строки появится:

```text
(.venv)
```

> Если PowerShell запрещает запуск скриптов, выполните:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 4. Установка зависимостей

```powershell
pip install -r requirements.txt
```

## Настройка конфигурации

Создайте файл `.env` из шаблона:

```powershell
Copy-Item .env.example .env
```

Откройте файл `.env` и укажите свои значения:

```env
APP_NAME=My Application
API_KEY=my-secret-api-key
```

### Переменные окружения

| Переменная | Описание |
|------------|-----------|
| APP_NAME | Название приложения |
| API_KEY | Секретный ключ приложения |

> Файл `.env` содержит локальные настройки и не должен попадать в репозиторий.

## Запуск приложения

```powershell
python .\main.py
```

## Пример успешного запуска

```text
Application: My Application
API_KEY loaded: True
```

## Пример ошибки

Если обязательная переменная отсутствует:

```text
Error: APP_NAME environment variable is not set.
```

## Структура проекта

```text
project/
│
├── .env.example
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Используемые библиотеки

- python-dotenv
- requests

## Автор

Polina Soboleva