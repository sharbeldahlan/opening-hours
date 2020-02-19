""" Tests for validation logic of the serializers """
import pytest

from application.serializers import DaySerializer


def test_serializers_invalid__value_non_integer():
    invalid_input = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [
            {'type': 'open', 'value': ":)"},
            {'type': 'close', 'value': 13000}
        ]
    }
    serializer = DaySerializer(data=invalid_input)
    assert not serializer.is_valid()
    assert 'A valid integer is required.' in serializer.errors['sunday'][0]['value'][0]


def test_serializers_invalid__value_not_in_range__below_minimum():
    invalid_input = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [
            {'type': 'open', 'value': -1},
            {'type': 'close', 'value': 13000}
        ]
    }
    serializer = DaySerializer(data=invalid_input)
    assert not serializer.is_valid()
    assert 'Ensure this value is greater than or equal to 0' in serializer.errors['sunday'][0]['value'][0]


def test_serializers_invalid__value_not_in_range__above_maximum():
    invalid_input = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [
            {'type': 'open', 'value': 13000},
            {'type': 'close', 'value': 99999}
        ]
    }
    serializer = DaySerializer(data=invalid_input)
    assert not serializer.is_valid()
    assert 'Ensure this value is less than or equal to 86399' in serializer.errors['sunday'][1]['value'][0]


def test_serializers_invalid__type_choice_invalid():
    invalid_input = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [
            {'type': 'in-between', 'value': 12000},
            {'type': 'close', 'value': 13000}
        ]
    }
    serializer = DaySerializer(data=invalid_input)
    assert not serializer.is_valid()
    assert '"in-between" is not a valid choice.' in serializer.errors['sunday'][0]['type'][0]


def test_serializers_invalid__type_key_missing():
    invalid_input = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [
            {'value': 12000},
            {'type': 'close', 'value': 13000}
        ]
    }
    serializer = DaySerializer(data=invalid_input)
    assert not serializer.is_valid()
    assert 'This field is required' in serializer.errors['sunday'][0]['type'][0]


def test_serializers_invalid__value_key_missing():
    invalid_input = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [
            {'type': 'open', 'value': 12000},
            {'type': 'close'}
        ]
    }
    serializer = DaySerializer(data=invalid_input)
    assert not serializer.is_valid()
    assert 'This field is required' in serializer.errors['sunday'][1]['value'][0]


def test_serializers_invalid__day_key_missing():
    # "monday" is missing
    invalid_input = {
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [
            {"type": "close", "value": 3600},
            {"type": "open", "value": 36000}
        ]
    }
    serializer = DaySerializer(data=invalid_input)
    assert not serializer.is_valid()
    assert 'This field is required' in serializer.errors['monday'][0]


def test_serializers_invalid__only_one_event():
    invalid_input = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [
            {'type': 'close', 'value': 13000}
        ]
    }
    serializer = DaySerializer(data=invalid_input)
    assert not serializer.is_valid()
    assert 'You must start and end a week with events of distinct types.' in serializer.errors['non_field_errors'][0]


def test_serializers_invalid__week_begins_and_ends_with_same_event_type():
    invalid_input = {
        "monday": [],
        "tuesday": [],
        "wednesday": [
            {'type': 'close', 'value': 12000},
            {'type': 'open', 'value': 13000}
        ],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [
            {'type': 'close', 'value': 13000}
        ]
    }
    serializer = DaySerializer(data=invalid_input)
    assert not serializer.is_valid()
    assert 'You must start and end a week with events of distinct types.' in serializer.errors['non_field_errors'][0]


def test_serializers_invalid__two_consecutive_open_times():
    invalid_input = {
        "monday": [
            {'type': 'open', 'value': 12000},
            {'type': 'open', 'value': 13000}
        ],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
    }
    serializer = DaySerializer(data=invalid_input)
    assert not serializer.is_valid()
    assert 'Cannot have two consecutive "open" times.' in serializer.errors['non_field_errors'][0]


@pytest.mark.parametrize(
    'day',
    ['monday', 'tuesday', 'wednesday',
     'thursday', 'friday', 'saturday', 'sunday']
)
def test_serializers_valid(day):
    """ Happy path """
    valid_data = {
        "monday": [],
        "tuesday": [
            {"type": "open", "value": 36000},
            {"type": "close", "value": 64800}
        ],
        "wednesday": [],
        "thursday": [
            {"type": "open", "value": 36000},
            {"type": "close", "value": 64800}
        ],
        "friday": [
            {"type": "open", "value": 36000}
        ],
        "saturday": [
            {"type": "close", "value": 3600},
            {"type": "open", "value": 36000}
        ],
        "sunday": [
            {"type": "close", "value": 3600},
            {"type": "open", "value": 43200},
            {"type": "close", "value": 75600}
        ]
    }
    serializer = DaySerializer(data=valid_data)
    assert serializer.is_valid()
    assert set(serializer.data.keys()) == {'monday', 'tuesday', 'wednesday',
                                           'thursday', 'friday', 'saturday', 'sunday'}

    # test that values of the serialized data match those of the input data
    assert serializer.data[day] == valid_data[day]
