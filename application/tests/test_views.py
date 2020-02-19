from unittest.mock import call
from unittest.mock import patch
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from application.views import index


def test_application_index_get__returns_200_and_correct_data():
    url = reverse('index')
    factory = APIRequestFactory()
    request = factory.get(url)
    response = index(request)
    assert response.status_code == 200
    assert response.data['message'] == 'index api view :)'


def test_application_index_post__serializer_invalid__returns_response_with_correct_data():
    url = reverse('index')
    factory = APIRequestFactory()
    request = factory.post(url, format='json')  # data is None, so serializer is invalid
    response = index(request)
    assert response.status_code == 400


@patch('application.views.to_human_readable_times')
@patch('application.views.DaySerializer')
def test_application_index_post__calls_to_human_readable_times_service(mock_serializer, mock_to_human_readable_times):
    url = reverse('index')
    factory = APIRequestFactory()
    request = factory.post(url, format='json')  # data is None but we're patching the serializer so it's fine
    index(request)
    assert mock_to_human_readable_times.call_count == 1
    assert mock_to_human_readable_times.call_args == call(mock_serializer().data)


@patch('application.views.to_human_readable_times')
@patch('application.views.DaySerializer')
def test_application_index_post__serializer_valid__returns_response_with_correct_data(mock_serializer,
                                                                                      mock_to_human_readable_times):
    mock_to_human_readable_times.return_value = "We're closed all week."
    url = reverse('index')
    factory = APIRequestFactory()
    request = factory.post(url, format='json')
    response = index(request)
    assert response.status_code == 200
    assert response.data == "We're closed all week."
