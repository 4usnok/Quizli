from fastapi import APIRouter

from app.core.config import AsyncSessionLocal
from app.crud import question
from app.schemas.question import QuestionCreate

router = APIRouter()


@router.get("/")
async def get_questions_list_route():
    """Получить список всех вопросов"""
    async with AsyncSessionLocal() as session:
        return await question.questions_list_crud(session)


@router.post("/")
async def create_question_route(question_data: QuestionCreate):
    """Создать новый вопрос"""
    async with AsyncSessionLocal() as session:
        return await question.create_question_crud(question_data, session)


@router.delete("/{id}")
async def delete_question_route(
    id: int,
):
    """Удалить вопрос (вместе с ответами)"""
    async with AsyncSessionLocal() as session:
        return await question.delete_question_crud(id, session)


@router.get("/{id}")
async def get_detail_question_route(
    id: int,
):
    """Получить вопрос и все ответы на него"""
    async with AsyncSessionLocal() as session:
        return await question.detail_question_crud(id, session)
