import pytest

from application.services import parse_input_times
from application.services import to_human_readable_times


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


def test_overflowing_closing_time():
    """
    Test case for when a restaurant does not close during the same day,
    the overflowing closing time needs to appear on the same day of the opening time.
    """
    new_data = data.copy()
    new_data['monday'] = [{
        'type': 'close',
        'value': 95400
    }]
    new_data['sunday'].append({
        'type': 'open',
        'value': 81000
    })
    parsed_times_dict = parse_input_times(new_data)
    assert parsed_times_dict['sunday'] == ['12 PM - 9 PM', '10:30 PM - 2:30 AM']


def test_to_human_readable_times():
    """ Test the main service end to end """
    expected_output = (
        'Monday: Closed\n'
        'Tuesday: 10 AM - 6 PM\n'
        'Wednesday: Closed\n'
        'Thursday: 10 AM - 6 PM\n'
        'Friday: 10 AM - 1 AM\n'
        'Saturday: 10 AM - 1 AM\n'
        'Sunday: 12 PM - 9 PM'
    )
    assert to_human_readable_times(data) == expected_output
