from sqlalchemy import Column, DateTime, Integer, String

from app.core.config import Base


class QuestionModel(Base):
    """Модель для вопросов"""

    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    text = Column(String(300), index=True)
    created_at = Column(DateTime, index=True)
