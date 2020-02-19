import pytest
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from application.views import index
from application.tests.integration_tests_payloads import first_valid_data
from application.tests.integration_tests_payloads import second_valid_data
from application.tests.integration_tests_payloads import first_invalid_data
from application.tests.integration_tests_payloads import second_invalid_data
from application.tests.integration_tests_payloads import third_invalid_data


@pytest.fixture(params=[first_valid_data, second_valid_data])
def valid_data_post_response(request):
    url = reverse('index')
    factory = APIRequestFactory()
    request = factory.post(path=url, data=request.param, format='json')
    response = index(request)
    return response


@pytest.fixture(params=[first_invalid_data, second_invalid_data, third_invalid_data])
def invalid_data_post_response(request):
    url = reverse('index')
    factory = APIRequestFactory()
    request = factory.post(path=url, data=request.param, format='json')
    response = index(request)
    return response


@pytest.fixture
def api_post_response():
    url = reverse('index')
    factory = APIRequestFactory()
    request = factory.post(path=url, data=first_valid_data, format='json')
    response = index(request)
    return response


def test_application_index_post__valid_and_invalid_data(valid_data_post_response, invalid_data_post_response):
    assert valid_data_post_response.status_code == 200
    assert invalid_data_post_response.status_code == 400


def test_application_index_post__end_to_end(api_post_response):
    expected_response_data = (
        'Monday: Closed\n'
        'Tuesday: 10 AM - 6 PM\n'
        'Wednesday: Closed\n'
        'Thursday: 10 AM - 6 PM\n'
        'Friday: 10 AM - 1 AM\n'
        'Saturday: 10 AM - 1 AM\n'
        'Sunday: 12 PM - 9 PM'
    )
    assert api_post_response.status_code == 200
    assert api_post_response.data == expected_response_data
