# import json
#
# from django.test import TestCase, Client
# from django.urls import reverse
#
# from my_mourse.models import Mourse
#
#
# class TestViews(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.home_url = reverse('mourse_home')
#         self.detail_url = reverse('mourse_details', args=['dummy-slug'])
#         # Mourse.objects.create()
#
#     def test_list_view_GET(self):
#         response = self.client.get(self.home_url)
#         print('LIST VIEW')
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, "my_mourse/mourse_list.html")
#
#     def test_mourse_detail_view_GET(self):
#         response = self.client.get(self.detail_url)
#         print('DETAIL VIEW')
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, "my_mourse/mourse_page_detail.html")
