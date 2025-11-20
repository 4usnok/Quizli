from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from app.core.config import Base


class AnswerModel(Base):
    """Модель для ответов"""

    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    question_id = Column(
        Integer, ForeignKey("questions.id", ondelete="CASCADE"), index=True
    )
    user_id = Column(String(36), index=True)
    text = Column(String(300))
    created_at = Column(DateTime, index=True)
