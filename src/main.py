from Calendar.CalendarEntry import CalendarEntry;
from Calendar.Calendar import Calendar;

def main():
    print("Hello, world!")
    # Entry for a probe at 30.04.2024 12:00 to 14:00 in PK1 
    entry = CalendarEntry("Probe", "20240430T120000", "20240430T140000", "PK1")
    # another a day later
    entry2 = CalendarEntry("Probe", "20240501T120000", "20240501T140000", "PK1")
    # Create a calendar and add the entries
    calendar = Calendar()
    calendar.add_entry(entry)
    calendar.add_entry(entry2)

    # Create a calendar based on the csv file
    calendar.from_csv("calendar.csv")

    #Create a ics file from the calendar
    calendar.to_ics("calendar.ics")


if __name__ == "__main__":
    main()
