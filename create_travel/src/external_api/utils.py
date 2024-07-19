from django.utils import timezone
from datetime import datetime, timedelta

def current_time():
    # Get the current time in UTC
    utc_now = timezone.now()
    
    # Convert it to the local time
    local_now = timezone.localtime(utc_now)
    dt = datetime.fromisoformat(str(local_now))

    # Format the datetime object to the desired string format
    formatted_datetime_str = dt.strftime('%Y-%m-%dT%H:%M:%S%z')

    # To insert the colon in the timezone offset (+0500 to +05:00)
    formatted_datetime_str = formatted_datetime_str[:-2] + ':' + formatted_datetime_str[-2:]

    # Format the local time in ISO 8601 format
    return formatted_datetime_str


def compare_delta_times(updated_at):
    # Get the current time
    now = timezone.now()
    
    # Define a past datetime for comparison
     
    
    # Calculate the difference between the two datetimes
    delta = now - updated_at
    
    # Define a timedelta to compare with
    threshold = timedelta(minutes=10)  # 10 minutes

    # Compare the timedelta differences
    if delta < threshold:
        return True
    else:
        return False