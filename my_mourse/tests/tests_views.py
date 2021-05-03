import json

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from my_mourse.models import Mourse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('mourse_home')
        self.detail_url = reverse('mourse_details', args=['dummy_mourse'])
        self.dummy_mourse = Mourse.objects.create(
            title='dummy_mourse',
            user=get_user_model().objects.first(),
            content='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            q_lectures=5
        )

    def test_list_view_GET(self):
        response = self.client.get(self.home_url)
        print('LIST VIEW')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "my_mourse/mourse_list.html")

    # def test_mourse_detail_view_GET(self):
    #     response = self.client.get(self.detail_url)
    #     print('DETAIL VIEW')
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "my_mourse/mourse_page_detail.html")
