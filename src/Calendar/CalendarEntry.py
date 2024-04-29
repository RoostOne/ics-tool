import datetime
import pytz

class CalendarEntry:
    # init method to create a new CalendarEntry object
    def __init__(self, title, start_time: datetime, end_time: datetime, location):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
    
    # string representation of the object
    def __str__(self):
        return f"{self.title} at {self.start_time} to {self.end_time} at {self.location}"
    
    # get the times in utc format
    @staticmethod
    def get_utc_times(other_time: datetime):
        # Define the local timezone as Europe/Berlin
        local = pytz.timezone("Europe/Berlin")
        
        # Define the UTC timezone
        utc = pytz.timezone("UTC")
        
        # Localize the input time to the Europe/Berlin timezone
        local_time = local.localize(other_time)
        
        # Convert the local time to UTC
        utc_time = local_time.astimezone(utc)
        
        # Return the time in UTC format
        return utc_time
    