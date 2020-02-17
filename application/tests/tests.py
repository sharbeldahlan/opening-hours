from django.urls import reverse
from rest_framework.test import APIRequestFactory

from application.views import index


def test_application_index__returns_200_and_correct_data():
    url = reverse('index')
    factory = APIRequestFactory()
    request = factory.get(url)
    response = index(request)
    assert response.status_code == 200
    assert response.data['message'] == 'index api view :)'
