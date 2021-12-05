import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))

from collective.settings import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_presence, process_ans


class TestClass(unittest.TestCase):
    """
    Класс с тестами
    """

    def test_def_presence(self):
        """
        Тест корректного запроса
        """
        test = create_presence()
        test[TIME] = 1.1  # Для уравнивания времени
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """
        Тест корректного разбора ответ 200
        """
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """
        Тест корректного разбора ответа 400
        """
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad request'}), '400 : Bad Request')

    def test_no_response(self):
        """
        Тст исключения без поля RESPONSE
        """
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
