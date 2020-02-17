import arrow


def format_time(timestamp: int) -> str:
    """
    Converts Unix timestamp to a human readable time
    in the format h:mm:ss AM/PM
               or h:mm AM/PM if the seconds are '00'
               or h AM/PM if the minutes are '00'
    """
    # Current time is in EET zone, so convert it to UTC
    current_time = arrow.Arrow.fromtimestamp(timestamp).to('UTC')
    formatted_time = current_time.format('h:mm:ss A')
    if current_time.format('ss') == '00':
        formatted_time = current_time.format('h:mm A')
        if current_time.format('mm') == '00':
            formatted_time = current_time.format('h A')

    return formatted_time
