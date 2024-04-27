# A Calenderclass that contains a list of CalendarEntry objects, which can print out the entries in a human-readable format and create a ics file from the entries.
from CalendarEntry import CalendarEntry


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
                f.write(f"DTSTART:{entry.start_time}\n")
                f.write(f"DTEND:{entry.end_time}\n")
                f.write(f"LOCATION:{entry.location}\n")
                f.write("END:VEVENT\n")
            f.write("END:VCALENDAR\n")
        

    # read the entries from a csv file and create a calendar from them
    # Date;Time;Location
    # Fr., 10.05.2024;15:15 - 17:45 Uhr;Probe (PK1)
    def from_csv(self, filename):
        with open(filename, "r") as f:
            for line in f:
                date, time, location = line.strip().split(";")
                entry = CalendarEntry(date, time, location)  # Assuming you have a CalendarEntry class
                self.add_entry(entry)