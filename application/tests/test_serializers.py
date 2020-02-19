""" Tests for validation logic of the serializers """
from application.serializers import DaySerializer


def test_serializers_invalid__value_non_integer():
    pass


def test_serializers_invalid__value_not_in_range__below_minimum():
    pass


def test_serializers_invalid__value_not_in_range__above_maximum():
    pass


def test_serializers_invalid__type_choice_invalid():
    pass


def test_serializers_invalid__type_key_missing():
    pass


def test_serializers_invalid__value_key_missing():
    pass


def test_serializers_invalid__day_key_missing():
    pass


def test_serializers_invalid__only_one_event():
    pass


def test_serializers_invalid__week_begins_and_ends_with_same_event_type():
    pass


def test_serializers_invalid__two_consecutive_open_times():
    pass


def test_serializers_valid():
    pass
