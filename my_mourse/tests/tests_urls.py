from django.test import SimpleTestCase
from django.urls import resolve, reverse

from my_mourse.views import (mourse_create_view,
                             mourse_delete_view,
                             mourse_detail_view,
                             mourse_list_view,
                             mourse_update_view)


class TestUrls(SimpleTestCase):
    def test_home_url(self):
        url = reverse('mourse_home')
        print("LIst")
        self.assertEquals(resolve(url).func, mourse_list_view)

    def test_create_url(self):
        url = reverse('create_mourse')
        print("Create")
        self.assertEquals(resolve(url).func, mourse_create_view)

    def test_retrieve_url(self):
        url = reverse('mourse_details', args=['dummy-slug'])
        print("REtrieve")
        self.assertEquals(resolve(url).func, mourse_detail_view)

    # def test_update_url(self):
        #
        # url = reverse('mourse_update_view', args=['dummy-slug'])
        # print("ANSWER", resolve(url))
        # self.assertEquals(resolve(url).func, update_mourse)

    # def test_delete_url(self):
    #     url = reverse('mourse_delete_view', args=['dummy-slug'])
    #     print("DElete")
    #     self.assertEquals(resolve(url).func, delete_mourse)
