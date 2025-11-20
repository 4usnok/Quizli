from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import AnswerModel
from app.models.question import QuestionModel
from app.schemas.question import QuestionCreate


async def questions_list_crud(session: AsyncSession):
    """Получение списка вопросов с использованием ORM SQLAlchemy."""
    view_list = await session.execute(select(QuestionModel))
    questions = view_list.scalars().all()
    return questions


async def create_question_crud(question_data: QuestionCreate, session: AsyncSession):
    """Создать новый вопрос с использованием ORM SQLAlchemy."""

    new_question = QuestionModel(text=question_data.text, created_at=datetime.now())

    session.add(new_question)
    await session.commit()  # Сохранение БД
    await session.refresh(new_question)  # Обновление БД
    return new_question


async def delete_question_crud(id: int, session: AsyncSession):
    """Удалить вопрос с использованием ORM SQLAlchemy."""
    del_question = await session.get(QuestionModel, id)
    if del_question:
        await session.delete(del_question)  # Удаление вопроса
        await session.commit()  # Сохранение БД
        return {"detail": "Deleted successfully"}
    else:
        return {"detail": "Question not found"}


async def detail_question_crud(id: int, session: AsyncSession):
    """
    Получить вопрос и все ответы на него
    с использованием ORM SQLAlchemy.
    """
    result = await session.execute(select(QuestionModel).where(QuestionModel.id == id))
    question = result.scalar_one_or_none()

    if not question:
        return None, None

    # Получаем ответы
    answers_result = await session.execute(
        select(AnswerModel).where(AnswerModel.question_id == id)
    )
    answers = answers_result.scalars().all()

    return question, answers
