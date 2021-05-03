from django.contrib.auth import get_user_model
from django.test import TestCase

from my_mourse.models import Mourse


class TestModel(TestCase):
    def setUp(self):
        self.dummy_mourse = Mourse.objects.create(
            title='dummy mourse',
            user=get_user_model().objects.first(),
            content='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            q_lectures=5
        )

    def test_mourse_is_assigned_slug_on_creation(self):
        self.assertEquals(self.dummy_mourse.slug, 'dummy-mourse')

