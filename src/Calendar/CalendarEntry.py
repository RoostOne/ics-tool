import datetime

class CalendarEntry:
    # init method to create a new CalendarEntry object
    def __init__(self, title, start_time: datetime, end_time: datetime, location):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
    