import asyncio
import unittest
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

from app.crud.question import create_question_crud
from app.schemas.question import QuestionCreate


class TestQuestion(unittest.TestCase):
    """Тесты для CRUD-операций `question`"""

    def setUp(self):
        """Подготовка данных для тестирования"""

        # 1. Мокаем сессию БД
        self.mock_session = AsyncMock()
        self.mock_session.commit = AsyncMock()
        self.mock_session.refresh = AsyncMock()
        self.mock_session.delete = AsyncMock()

        # 2. тестовые данные для создания ответа
        self.test_question_data = QuestionCreate(text="test_text")

        # 3. Замоканный результат
        self.mock_question_result = MagicMock()
        self.mock_question_result.id = 1
        self.mock_question_result.text = "test_text"
        self.mock_question_result.created_at = datetime.now()

    def test_create_question_crud(self):
        """Тестирование создания нового вопроса"""

        # Вызываем CRUD
        result = asyncio.run(
            create_question_crud(self.test_question_data, self.mock_session)
        )

        # Проверяем
        self.mock_session.add.assert_called_once()
        self.mock_session.commit.assert_called_once()
        self.assertEqual(result.text, "test_text")
