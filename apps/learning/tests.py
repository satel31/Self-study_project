from rest_framework import status
from rest_framework.test import APITestCase

from apps.learning.models import Section, Material, Test, Question, Answer, UserAnswer
from apps.user.models import User


class SectionTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/learning/'
        self.user = User.objects.create(email='test@example.com', password='test', role='moderator')
        self.data = {
            'section_name': 'test',
            'description': 'test',
        }

        self.section = Section.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_section(self):
        """Section creation testing """
        data = {
            'section_name': 'test1',
            'description': 'test',
        }
        response = self.client.post(f'{self.url}add_section/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Section.objects.all().count(), 2)

    def test_2_list_section(self):
        """Section list testing """
        response = self.client.get(f'{self.url}sections/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()['results'],
            [{'id': self.section.pk, 'material_count': 0, 'material': [], 'section_name': 'test', 'preview': None,
              'description': 'test'}]
        )

    def test_3_retrieve_section(self):
        """Section retrieve testing """

        response = self.client.get(f'{self.url}sections/{self.section.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.section.pk, 'material_count': 0, 'material': [], 'section_name': 'test', 'preview': None,
             'description': 'test'}
        )

    def test_4_update_section(self):
        """Section update testing """
        data = {
            'section_name': 'test1',
            'description': 'test1',
        }

        response = self.client.put(f'{self.url}sections/update/{self.section.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.section.pk, 'material_count': 0, 'material': [], 'section_name': 'test1', 'preview': None,
             'description': 'test1'}
        )

    def test_5_update_partial_section(self):
        """Section partial update testing """
        data = {
            'section_name': 'test1'
        }
        response = self.client.patch(f'{self.url}sections/update/{self.section.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.section.pk, 'material_count': 0, 'material': [], 'section_name': 'test1', 'preview': None,
             'description': 'test'}
        )

    def test_6_destroy_section(self):
        """Section destroying testing """
        response = self.client.delete(f'{self.url}sections/delete/{self.section.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Section.objects.all().exists())

    def test_7_str_section(self):
        """Section str method testing"""
        self.assertEqual(str(self.section), self.section.section_name)


class MaterialTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/learning/'
        self.section = Section.objects.create(section_name='test')
        self.user = User.objects.create(email='test@example.com', password='test', role='moderator')
        self.data = {
            'material_name': 'test',
            'description': 'test',
            'text': 'test',
            'section': self.section,
        }

        self.material = Material.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_material(self):
        """Material creation testing """
        data = {
            'material_name': 'test1',
            'description': 'test1',
            'text': 'test1',
            'section': self.section.section_name,
        }
        response = self.client.post(f'{self.url}add_material/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Material.objects.all().count(), 2)

    def test_2_list_material(self):
        """Material list testing """
        response = self.client.get(f'{self.url}materials/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{'id': self.material.pk, 'tests': [], 'test_count': 0, 'section': 'test', 'material_name': 'test',
              'description': 'test', 'preview': None, 'text': 'test'}]
        )

    def test_3_retrieve_material(self):
        """Material retrieve testing """

        response = self.client.get(f'{self.url}materials/{self.material.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.material.pk, 'tests': [], 'test_count': 0, 'section': 'test', 'material_name': 'test',
             'description': 'test', 'preview': None, 'text': 'test'}
        )

    def test_4_update_material(self):
        """Material update testing """
        data = {
            'material_name': 'test1',
            'description': 'test',
            'text': 'test',
            'section': self.section.section_name,
        }

        response = self.client.put(f'{self.url}materials/update/{self.material.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.material.pk, 'tests': [], 'test_count': 0, 'section': 'test', 'material_name': 'test1',
             'description': 'test', 'preview': None, 'text': 'test'}
        )

    def test_5_update_partial_material(self):
        """Material partial update testing """
        data = {
            'material_name': 'test1'
        }
        response = self.client.patch(f'{self.url}materials/update/{self.material.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.material.pk, 'tests': [], 'test_count': 0, 'section': 'test', 'material_name': 'test1',
             'description': 'test', 'preview': None, 'text': 'test'}
        )

    def test_6_destroy_material(self):
        """Material destroying testing """
        response = self.client.delete(f'{self.url}materials/delete/{self.material.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Material.objects.all().exists())

    def test_7_str_material(self):
        """Material str method testing"""
        self.assertEqual(str(self.material), self.material.material_name)


class TestTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/learning/'
        self.material = Material.objects.create(material_name='test')
        self.user = User.objects.create(email='test@example.com', password='test', role='moderator')
        self.data = {
            'test_name': 'test',
            'description': 'test',
            'material': self.material,
        }

        self.test = Test.objects.create(**self.data)
        self.question = Question.objects.create(test=self.test, text='test')
        self.answer = Answer.objects.create(question=self.question, text='test')
        self.user_answer = UserAnswer.objects.create(answer='test', user=self.user, question=self.question,
                                                     is_passed=True)
        self.client.force_authenticate(user=self.user)

    def test_1_create_test(self):
        """Test creation testing """
        data = {
            'test_name': 'test',
            'description': 'test',
            'material': self.material.pk,
        }
        response = self.client.post(f'{self.url}add_test/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Test.objects.all().count(), 2)

    def test_2_list_test(self):
        """Test list testing """
        response = self.client.get(f'{self.url}tests/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{'id': self.test.pk, 'question_count': 1, 'right_answers': 1,
              'questions': [{'id': self.question.pk, 'test': self.test.pk, 'text': 'test'}], 'test_name': 'test',
              'description': 'test', 'material': self.material.pk}]
        )

    def test_3_retrieve_test(self):
        """Test retrieve testing """

        response = self.client.get(f'{self.url}tests/{self.test.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.test.pk, 'question_count': 1, 'right_answers': 1,
             'questions': [{'id': self.question.pk, 'test': self.test.pk, 'text': 'test'}], 'test_name': 'test',
             'description': 'test', 'material': self.material.pk}
        )

    def test_4_update_test(self):
        """Test update testing """
        data = {
            'test_name': 'test1',
            'description': 'test',
            'material': self.material.pk,
        }

        response = self.client.put(f'{self.url}tests/update/{self.test.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.test.pk, 'question_count': 1, 'right_answers': 1,
             'questions': [{'id': self.question.pk, 'test': self.test.pk, 'text': 'test'}], 'test_name': 'test1',
             'description': 'test', 'material': self.material.pk}
        )

    def test_5_update_partial_test(self):
        """Test partial update testing """
        data = {
            'test_name': 'test1'
        }
        response = self.client.patch(f'{self.url}tests/update/{self.test.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.test.pk, 'question_count': 1, 'right_answers': 1,
             'questions': [{'id': self.question.pk, 'test': self.test.pk, 'text': 'test'}], 'test_name': 'test1',
             'description': 'test', 'material': self.material.pk}
        )

    def test_6_destroy_test(self):
        """Test destroying testing """
        response = self.client.delete(f'{self.url}tests/delete/{self.test.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Test.objects.all().exists())

    def test_7_str_test(self):
        """Test str method testing"""
        self.assertEqual(str(self.test), self.test.test_name)


class QuestionTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/learning/'
        self.test = Test.objects.create(test_name='test')
        self.user = User.objects.create(email='test@example.com', password='test', role='moderator')
        self.data = {
            'test': self.test,
            'text': 'test'
        }

        self.question = Question.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_question(self):
        """Question creation testing """
        data = {
            'test': self.test.pk,
            'text': 'test'
        }
        response = self.client.post(f'{self.url}add_question/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Question.objects.all().count(), 2)

    def test_2_list_question(self):
        """Question list testing """
        response = self.client.get(f'{self.url}questions/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{'id': self.question.pk, 'text': 'test', 'test': self.test.pk}]
        )

    def test_3_retrieve_question(self):
        """Question retrieve testing """

        response = self.client.get(f'{self.url}questions/{self.question.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.question.pk, 'text': 'test', 'test': self.test.pk}
        )

    def test_4_update_question(self):
        """Question update testing """
        data = {
            'test': self.test.pk,
            'text': 'test1'
        }

        response = self.client.put(f'{self.url}questions/update/{self.question.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.question.pk, 'text': 'test1', 'test': self.test.pk}
        )

    def test_5_update_partial_question(self):
        """Question partial update testing """
        data = {
            'text': 'test1'
        }
        response = self.client.patch(f'{self.url}questions/update/{self.question.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.question.pk, 'text': 'test1', 'test': self.test.pk}
        )

    def test_6_destroy_question(self):
        """Question destroying testing """
        response = self.client.delete(f'{self.url}questions/delete/{self.question.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Question.objects.all().exists())

    def test_7_str_question(self):
        """Question str method testing"""
        self.assertEqual(str(self.question), f'Question of {self.question.test}')

    def test_8_retrieve_question_w_answer(self):
        """Question retrieve testing """
        self.answer = Answer.objects.create(question=self.question, text='test')
        self.user_answer = UserAnswer.objects.create(answer='test', user=self.user, question=self.question,
                                                     is_passed=True)
        response = self.client.get(f'{self.url}questions/{self.question.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.question.pk, 'user_answers': [
                {'id': self.user_answer.pk, 'answer': 'test', 'is_passed': True, 'user': self.user.pk,
                 'question': self.question.pk}],
             'text': 'test', 'test': self.test.pk}
        )


class AnswerTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/learning/'
        self.test = Test.objects.create(test_name='test')
        self.question = Question.objects.create(test=self.test, text='test')
        self.user = User.objects.create(email='test@example.com', password='test', role='moderator')
        self.data = {
            'question': self.question,
            'text': 'test'
        }

        self.answer = Answer.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_answer(self):
        """Answer creation testing """
        data = {
            'question': self.question.pk,
            'text': 'test'
        }
        response = self.client.post(f'{self.url}add_answer/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Answer.objects.all().count(), 2)

    def test_2_update_answer(self):
        """Answer update testing """
        data = {
            'question': self.question.pk,
            'text': 'test1'
        }

        response = self.client.put(f'{self.url}answers/update/{self.answer.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.answer.pk, 'text': 'test1', 'question': self.question.pk}
        )

    def test_3_update_partial_answer(self):
        """Answer partial update testing """
        data = {
            'text': 'test1'
        }
        response = self.client.patch(f'{self.url}answers/update/{self.answer.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.answer.pk, 'text': 'test1', 'question': self.question.pk}
        )

    def test_4_str_answer(self):
        """Answer str method testing"""
        self.assertEqual(str(self.answer), f'Answer of {self.answer.question}')


class UserAnswerTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/learning/'
        self.test = Test.objects.create(test_name='test')
        self.question = Question.objects.create(test=self.test, text='test')
        self.answer = Answer.objects.create(question=self.question, text='test')
        self.user = User.objects.create(email='test@example.com', password='test', role='moderator')
        self.data = {
            'answer': 'test',
            'user': self.user,
            'question': self.question
        }

        self.user_answer = UserAnswer.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_user_answer(self):
        """UserAnswer creation testing """
        data = {
            'answer': 'test',
            'user': self.user.pk,
            'question': self.question.pk
        }
        response = self.client.post(f'{self.url}add_user_answer/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(UserAnswer.objects.all().count(), 2)

    def test_2_destroy_user_answer(self):
        """UserAnswer destroying testing """
        response = self.client.delete(f'{self.url}user_answer/delete/{self.user_answer.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(UserAnswer.objects.all().exists())

    def test_3_str_answer(self):
        """UserAnswer str method testing"""
        self.assertEqual(str(self.user_answer),
                         f'{self.user_answer.user} {self.user_answer.question} {self.user_answer.answer}')

    def test_4_create_user_answer_false(self):
        """False UserAnswer creation testing """
        data = {
            'answer': 'test1',
            'user': self.user.pk,
            'question': self.question.pk
        }
        response = self.client.post(f'{self.url}add_user_answer/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertFalse(UserAnswer.objects.last().is_passed)
