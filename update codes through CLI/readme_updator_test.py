import unittest
from quera_readme_updator import *


test_link = 'https://quera.org/problemset/9024'


class QueraQuestionTestCase(unittest.TestCase):

    question_test_instance = QueraQuestion(test_link)


    def test_quera_question(self):
        quera_question = QueraQuestion(question_link=test_link)

    def test_get_quera_id(self):
        quera_id = QueraQuestionTestCase.question_test_instance.get_quera_id()
        self.assertEqual(quera_id, '9024')

    def test_get_question_tags(self):
        question_tags = QueraQuestionTestCase.question_test_instance.get_tags()
        self.assertEqual(question_tags, ['Dynamic Programming',
        'Greedy',])



if __name__ == '__main__':
    unittest.main()
