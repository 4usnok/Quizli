from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.answer import AnswerModel
from app.schemas.answer import AnswerCreate


async def create_answer_crud(
    question_id: int, answer_data: AnswerCreate, session: AsyncSession
):
    """Добавить новый ответ к вопросу с использованием ORM SQLAlchemy."""

    new_answer = AnswerModel(
        question_id=question_id,
        user_id=answer_data.user_id,
        text=answer_data.text,
        created_at=datetime.now(),
    )

    session.add(new_answer)
    await session.commit()  # Сохранение БД
    await session.refresh(new_answer)  # Обновление БД
    return new_answer


async def get_detail_answer_crud(id: int, session: AsyncSession):
    """Получает конкретный ответ с использованием ORM SQLAlchemy."""
    det_answer = await session.get(AnswerModel, id)
    if not det_answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return det_answer


async def delete_answer_crud(id: int, session: AsyncSession):
    """Удаляет ответ с использованием ORM SQLAlchemy."""
    del_answer = await session.get(AnswerModel, id)
    if del_answer:
        await session.delete(del_answer)
        await session.commit()  # Сохранение БД
        return {"detail": "Deleted successfully"}
    else:
        return {"detail": "Answer not found"}
