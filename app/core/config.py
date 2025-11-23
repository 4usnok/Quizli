import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

load_dotenv()

# Переменные окружения
USERNAME_DB = os.getenv("USERNAME_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")
NAME_DB = os.getenv("NAME_DB")
HOST_DB = os.getenv("HOST_DB")

# URL для подключения к PostgreSQL
async_postgresql_url = (
    f"postgresql+asyncpg://{USERNAME_DB}:{PASSWORD_DB}@{HOST_DB}:5432/{NAME_DB}"
)

# движок SQLAlchemy
engine = create_async_engine(async_postgresql_url, echo=True)

# Фабрика сессий для взаимодействия с БД
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# Базовый класс для моделей
Base = declarative_base()
