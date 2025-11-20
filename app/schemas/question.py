from datetime import datetime

from pydantic import BaseModel


class Question(BaseModel):
    """SQLAlchemy модель для вопроса"""

    id: int
    text: str
    created_at: datetime

    class Config:
        from_attributes = True  # для конвертации ORM → Pydantic


class QuestionCreate(BaseModel):
    """SQLAlchemy модель для создания нового вопроса"""

    text: str
