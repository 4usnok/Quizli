from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import answer
from app.models.question import QuestionModel
from app.schemas.answer import AnswerCreate


class AnswerService:
    @staticmethod
    async def create_answer_with_validation(
        question_id: int, answer_data: AnswerCreate, session: AsyncSession
    ):
        """ВАЛИДАЦИЯ: проверка, что вопрос существует"""
        question = await session.get(QuestionModel, question_id)
        if not question:
            raise HTTPException(404, "Question not found")

        # Вызываем CRUD без валидации
        return await answer.create_answer_crud(question_id, answer_data, session)
