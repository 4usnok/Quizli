from datetime import datetime

from pydantic import BaseModel


class AnswerSchemas(BaseModel):
    """SQLAlchemy модель для ответа"""

    id: int
    question_id: int
    user_id: str
    text: str
    created_at: datetime

    class Config:
        from_attributes = True  # для конвертации ORM → Pydantic


class AnswerCreate(BaseModel):
    """SQLAlchemy модель для создания нового ответа"""

    user_id: str
    text: str
