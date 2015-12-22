from django.core.urlresolvers import reverse
from django.test import TestCase


class ViewTest(TestCase):

    def test_projects_view(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
