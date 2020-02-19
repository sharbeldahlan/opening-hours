first_valid_data = {
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


second_valid_data = {
        "monday": [],
        "tuesday": [
            {"type": "open", "value": 36000},
            {"type": "close", "value": 64800}
        ],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
}


first_invalid_data = {
        "monday": [],
}

second_invalid_data = {
        "monday": [],
        "tuesday": [
            {"type": "open", "value": 36000},
            {"type": "open", "value": 64800}
        ],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
}

third_invalid_data = {
        "monday": [],
        "tuesday": [
            {"type": "open", "value": 36000},
            {"type": "close", "value": 64800}
        ],
        "wednesday": [],
        "thursday": [
            {"type": "open", "value": 36000},
        ],
        "friday": [],
        "saturday": [],
        "sunday": []
}
