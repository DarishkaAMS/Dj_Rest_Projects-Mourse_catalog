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
        self.assertEquals(resolve(url).func, mourse_list_view)

    def test_create_url(self):
        url = reverse('create_mourse')
        self.assertEquals(resolve(url).func, mourse_create_view)

    def test_retrieve_url(self):
        url = reverse('mourse_details', args=['dummy-slug'])
        self.assertEquals(resolve(url).func, mourse_detail_view)

    def test_update_url(self):
        url = reverse('update_mourse', args=['dummy-slug'])
        self.assertEquals(resolve(url).func, mourse_update_view)

    def test_delete_url(self):
        url = reverse('delete_mourse', args=['dummy-slug'])
        self.assertEquals(resolve(url).func, mourse_delete_view)
