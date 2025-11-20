from fastapi import APIRouter

from app.core.config import AsyncSessionLocal
from app.crud import answer
from app.schemas.answer import AnswerCreate
from app.services.answer_service import AnswerService

router = APIRouter()


@router.get("/answers/{id}")
async def get_detail_answer_route(id: int):
    """Получить конкретный ответ"""
    async with AsyncSessionLocal() as session:
        return await answer.get_detail_answer_crud(id, session)


@router.delete("/answers/{id}")
async def delete_answer_route(id: int):
    """Удалить ответ"""
    async with AsyncSessionLocal() as session:
        return await answer.delete_answer_crud(id, session)


@router.post("/questions/{id}/answers/")
async def add_answers_route(id: int, answer_data: AnswerCreate):
    """Добавить ответ к вопросу"""
    async with AsyncSessionLocal() as session:
        return await AnswerService.create_answer_with_validation(
            id, answer_data, session
        )
