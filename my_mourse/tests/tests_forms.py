from django.contrib.auth import get_user_model
from django.test import TestCase

from my_mourse.forms import MourseForm


class TestForm(TestCase):

    def test_expense_form_valid_data(self):
        form = MourseForm(data={
            'title': 'dummy mourse',
            'user': get_user_model().objects.first(),
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'q_lectures': 5
        })

        self.assertEquals(form.is_valid(), True)
