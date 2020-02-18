import pytest

from application.services import parse_input_times


# Example payload data
data = {
    "monday": [],
    "tuesday": [
        {
            "type": "open",
            "value": 36000
        },
        {
            "type": "close",
            "value": 64800
        }
    ],
    "wednesday": [],
    "thursday": [
        {
            "type": "open",
            "value": 36000
        },
        {
            "type": "close",
            "value": 64800
        }
    ],
    "friday": [
        {
            "type": "open",
            "value": 36000
        }
    ],
    "saturday": [
        {
            "type": "close",
            "value": 3600
        },
        {
            "type": "open",
            "value": 36000
        }
    ],
    "sunday": [
        {
            "type": "close",
            "value": 3600
        },
        {
            "type": "open",
            "value": 43200
        },
        {
            "type": "close",
            "value": 75600
        }
    ]
}


@pytest.mark.parametrize(
    "day, times",
    [
        ('monday', []),
        ('tuesday', ['10 AM - 6 PM']),
        ('wednesday', []),
        ('thursday', ['10 AM - 6 PM']),
        ('friday', ['10 AM - 1 AM']),
        ('saturday', ['10 AM - 1 AM']),
        ('sunday', ['12 PM - 9 PM'])
    ]
)
def test_parse_input_times(day, times):
    """ Test for the service's parsing function """
    parsed_times_dict = parse_input_times(data)
    assert parsed_times_dict[day] == times

