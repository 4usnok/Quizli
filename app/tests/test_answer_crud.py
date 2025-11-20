import asyncio
import unittest
from datetime import datetime
from unittest.mock import AsyncMock


from app.crud.answer import create_answer_crud, get_detail_answer_crud
from app.models.answer import AnswerModel
from app.schemas.answer import AnswerCreate


class TestAnswerWithMocks(unittest.TestCase):
    """Тесты с моками БД"""

    def setUp(self):
        """Подготовка данных для тестов"""

        # 1. Мокаем сессию БД
        self.mock_session = AsyncMock()
        self.mock_session.commit = AsyncMock()
        self.mock_session.refresh = AsyncMock()
        self.mock_session.delete = AsyncMock()

        # 2. Создаем тестовые данные для создания ответа
        self.test_answer_data = AnswerCreate(
            question_id=1, user_id="test_id", text="test_text"
        )

        # 3. ответ из БД
        self.mock_answer = AnswerModel(
            id=1,
            question_id=1,
            user_id="test-user",
            text="Тестовый ответ",
            created_at=datetime.now(),
        )

    def test_create_answer(self):
        """Тест создания ответа"""

        # Вызываем CRUD
        result = asyncio.run(
            create_answer_crud(
                question_id=1,
                answer_data=self.test_answer_data,
                session=self.mock_session,
            )
        )

        # Проверяем
        self.mock_session.add.assert_called_once()
        self.mock_session.commit.assert_called_once()
        self.assertEqual(result.text, "test_text")

    def test_get_answer_exists(self):
        """Тест получения существующего ответа"""

        # Настраиваем мок, чтобы вернуть ответ
        self.mock_session.get.return_value = self.mock_answer

        result = asyncio.run(get_detail_answer_crud(1, self.mock_session))

        # Проверяем
        self.assertEqual(result.id, 1)
        self.assertEqual(result.text, "Тестовый ответ")
