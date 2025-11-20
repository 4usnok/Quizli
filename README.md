# Quizli
API-сервис для вопросов и ответов

# Стек
`Fastapi, PostgreSQL, Docker, Alembic, SQLAlchemy`

# Инструкция по установке и использованию разработанного функционала приложения
1. Клонируйте репозиторий:
```
git clone https://github.com/4usnok/Quizli.git
```
2. Активируйте виртуальное окружение poetry:
```
poetry shell
```
3. Установите зависимости poetry:
```
poetry install
```

# Управление приложением  
Запуск -> `uvicorn main:app --reload`

# Содержание проекта
## Директория app
Предназначена для компонентов приложения:
1. `models` -> Pydantic модели:  
1.1. `answer.py` -> модели для ответов  
1.2. `question.py` -> модели для вопросов  
  
2. `schemas` -> SQLAlchemy модели:  
2.1. `answer.py` -> модели для ответов  
2.2. `question.py` -> модели для вопросов  
  
3. `services` -> бизнес логика:  
3.1. `answer_service.py` -> проверка, что вопрос существует
  
4. `core` -> инфраструктура приложения:  
4.1. `config.py` -> Настройка БД  
  
5. `crud` -> CRUD-логика  
5.1. `answer.py` -> CRUD для ответов  
5.2. `question.py` -> CRUD для вопросов  
  
6. `routers` -> API эндпоинты/роутеры:  
6.1. `answer.py` -> api ответов  
6.2. `question.py` -> api вопросов  
  
7. `tests` -> тесты:  
7.1. `test_question_crud.py` -> тесты для вопросов  
7.2. `test_answer_crud.py` -> тесты для ответов

## Прочие файлы файлы
1. `.env.sample` -> шаблон файла `.env` (заполняется в первую очередь)  
2. `.flake8` -> настройки для линтера `flake8`  
3. `.gitignore` -> текстовый файл позволяет контролировать, что следует игнорировать и не отслеживать  
4. `alembic.ini` -> настройки `alembic`  
5. `main.py` -> главный файл для запуска приложения  
6. `docker-compose.yml` -> оркестрация нескольких сервисов  
7. `Dockerfile` -> инструкция по сборке образа  

# Полезные команды
1. Создание миграций -> `alembic revision --autogenerate -m "Create Quizli Table"`
2. Применение миграций -> `alembic upgrade head`
3. Создания файла с покрытием .coverage -> `coverage html `
4. Посмотреть покрытие unit-тестами -> `coverage report`
5. Тестирование приложения -> `python -m unittest -v`