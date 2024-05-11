# A Calenderclass that contains a list of CalendarEntry objects, which can print out the entries in a human-readable format and create a ics file from the entries.
from datetime import datetime
import pandas as pd

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
                f.write(f"DTSTAMP:{datetime.now().strftime('%Y%m%dT%H%M%SZ')}\n")
                start_time_utc = entry.get_utc_times(entry.start_time)
                end_time_utc = entry.get_utc_times(entry.end_time) 
                f.write(f"DTSTART:{start_time_utc.strftime('%Y%m%dT%H%M%SZ')}\n")
                f.write(f"DTEND:{end_time_utc.strftime('%Y%m%dT%H%M%SZ')}\n")
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

    # from csv but with a file
    def from_csv(self, file):
        next(file)
        for line in file:
            # line as string
            line = line.decode("utf-8")
            date, time, title, location = line.strip().split(";")
            start_time, end_time = self.get_start_end_time(time, date)
            entry = CalendarEntry(title, start_time, end_time, location)
            self.add_entry(entry)
    
    # function gets a string of the date and returns start and end time as datetime objects
    def get_start_end_time(self, time_str, date_str):

        # Get the date from date_str
        # remove the weekday from the beginning of the string
        date = datetime.strptime(date_str.split(",")[1], " %d.%m.%Y")

        # Remove the "Uhr" from the end of the string
        time_str = time_str.replace(" Uhr", "")

        # Check if the time string contains a "-" and add the same time to the end if it doesn't
        if(time_str.find("-") == -1):
            time_str = time_str + " - " + time_str
        start_time, end_time = time_str.replace(" ","").split("-")
        
        # add minutes to the end time if there are only hours
        if start_time.find(":") == -1:
            start_time = start_time + ":00"
        if end_time.find(":") == -1:
            end_time = end_time + ":00"
        
       
        start_time = datetime.strptime(start_time, "%H:%M")
        end_time = datetime.strptime(end_time, "%H:%M")
        
        # Combine the date with the start and end time
        start_time = datetime.combine(date, start_time.time())
        end_time = datetime.combine(date, end_time.time())

        # add 1 hour to the end time if it is the same as the start time
        if start_time == end_time:
            end_time = end_time.replace(hour=end_time.hour + 1)
        return start_time, end_time
    
    # from dataframe to calendar entries
    def from_df(self, df):
        for index, row in df.iterrows():
            start_time = datetime.strptime(row["Date"] + " " + row["Start Time"], "%d.%m.%Y %H:%M")
            end_time = datetime.strptime(row["Date"] + " " + row["End Time"], "%d.%m.%Y %H:%M")
            entry = CalendarEntry(row["Title"], start_time, end_time, row["Location"])
            print(entry)
            self.add_entry(entry)
        
    # Calendar to dataframe Date; Start Time; End Time; Title; Location
    def to_df(self):
        data = {
            "Date": [entry.start_time.strftime("%d.%m.%Y") for entry in self.entries],
            "Start Time": [entry.start_time.strftime("%H:%M") for entry in self.entries],
            "End Time": [entry.end_time.strftime("%H:%M") for entry in self.entries],
            "Title": [entry.title for entry in self.entries],
            "Location": [entry.location for entry in self.entries]
        }
        df = pd.DataFrame(data)
        return df