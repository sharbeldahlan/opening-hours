from rest_framework import serializers

from application.constants import EVENT_TYPE_CHOICES


class EventSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=EVENT_TYPE_CHOICES)
    value = serializers.IntegerField(min_value=0, max_value=86399)


class DaySerializer(serializers.Serializer):
    monday = EventSerializer(many=True)
    tuesday = EventSerializer(many=True)
    wednesday = EventSerializer(many=True)
    thursday = EventSerializer(many=True)
    friday = EventSerializer(many=True)
    saturday = EventSerializer(many=True)
    sunday = EventSerializer(many=True)

    def validate(self, data: dict) -> dict:
        """
        Check for the following cases:
            1) If there are two consecutive events of the same type --> raise error.
            2) If first and last event types of the week are the same, or
            3)     there is only one event in the whole week --> raise error.
        """
        first_event_type = None
        previous_event_type = None
        for day, events in data.items():
            for event in events:
                if event['type'] == previous_event_type:
                    raise serializers.ValidationError(f'Cannot have two consecutive "{event["type"]}" times.')
                else:
                    previous_event_type = event['type']

                if first_event_type is None:
                    first_event_type = event['type']
        if first_event_type == previous_event_type:
            raise serializers.ValidationError('You must start and end a week with events of distinct types.')

        return data
