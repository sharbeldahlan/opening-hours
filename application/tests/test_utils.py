import pytest

from application.utils import format_output
from application.utils import format_time
from application.utils import format_time_range


@pytest.mark.parametrize(
    "unix_timestamp, formatted_time",
    [
        (32400, '9 AM'),
        (37800, '10:30 AM'),
        (86399, '11:59:59 PM'),
        (72000, '8 PM'),
        (32700, '9:05 AM'),
        (32405, '9:00:05 AM'),
        (0, '12 AM')
    ]
)
def test_format_time(unix_timestamp, formatted_time):
    assert format_time(unix_timestamp) == formatted_time


def test_format_time_range():
    assert format_time_range('12 PM', '9:30 AM') == '12 PM - 9:30 AM'


def test_format_output():
    parsed_times_dict = {
        'monday': [],
        'tuesday': ['10 AM - 6 PM'],
        'wednesday': [],
        'thursday': ['10 AM - 6 PM'],
        'friday': ['10 AM - 1 AM'],
        'saturday': ['10 AM - 1 AM'],
        'sunday': ['12 PM - 9 PM', '10:30 PM - 2:30 AM']
    }
    expected_output = (
        'Monday: Closed\n'
        'Tuesday: 10 AM - 6 PM\n'
        'Wednesday: Closed\n'
        'Thursday: 10 AM - 6 PM\n'
        'Friday: 10 AM - 1 AM\n'
        'Saturday: 10 AM - 1 AM\n'
        'Sunday: 12 PM - 9 PM, 10:30 PM - 2:30 AM'
    )
    assert format_output(parsed_times_dict) == expected_output
