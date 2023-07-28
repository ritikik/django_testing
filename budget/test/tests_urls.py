from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import project_list, project_detail

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, project_list)

    def test_detail_url_is_resolved(self):
        url = reverse('detail', args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, project_detail)