# A Calenderclass that contains a list of CalendarEntry objects, which can print out the entries in a human-readable format and create a ics file from the entries.
from datetime import datetime

from Calendar.CalendarEntry import CalendarEntry

class Calendar:
    def __init__(self):
        self.entries = []
    
    def add_entry(self, entry):
        self.entries.append(entry)
    
    def __str__(self):
        return "\n".join([str(entry) for entry in self.entries])
    
    def to_ics(self, filename):
        with open(filename, "w") as f:
            f.write("BEGIN:VCALENDAR\n")
            f.write("VERSION:2.0\n")
            f.write("PRODID:-//hacksw/handcal//NONSGML v1.0//EN\n")
            for entry in self.entries:
                f.write("BEGIN:VEVENT\n")
                f.write(f"SUMMARY:{entry.title}\n")
                # datetime objects to ical format
                f.write(f"DTSTAMP:{datetime.now().strftime('%Y%m%dT%H%M%SZ')}\n")
                f.write(f"DTEND:{entry.end_time}\n")
                f.write(f"LOCATION:{entry.location}\n")
                f.write("END:VEVENT\n")
            f.write("END:VCALENDAR\n")
        

    # read the entries from a csv file and create a calendar from them
    # Date;Time;Location
    # Fr., 10.05.2024;15:15 - 17:45 Uhr;Probe (PK1)
    def from_csv(self, filename):
        with open(filename, "r") as f:
            # Skip the header
            next(f)
            for line in f:
                date, time, title, location = line.strip().split(";")
                start_time, end_time = self.get_start_end_time(time, date)
                entry = CalendarEntry(title, start_time, end_time, location)  # Assuming you have a CalendarEntry class
                self.add_entry(entry)
    
    # function gets a string of the date and returns start and end time as datetime objects
    def get_start_end_time(self, time_str, date_str):

        # Get the date from date_str
        # remove the weekday from the beginning of the string
        date = datetime.strptime(date_str.split(",")[1], " %d.%m.%Y")

        # Remove the "Uhr" from the end of the string
        time_str = time_str.replace(" Uhr", "")
        
        print(time_str) 

        start_time, end_time = time_str.replace(" ", "").split("-")
        
        # Get the start and end time as datetime objects
        # try multiple formats "HH:MM" and "H:"
        try:
            start_time = datetime.strptime(start_time, "%H:%M")
            end_time = datetime.strptime(end_time, "%H:%M")
        except:
            start_time = datetime.strptime(start_time, "%H")
            end_time = datetime.strptime(end_time, "%H")
        
        # Combine the date with the start and end time
        start_time = datetime.combine(date, start_time.time())
        end_time = datetime.combine(date, end_time.time())
        
        return start_time, end_time