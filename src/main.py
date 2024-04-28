from Calendar.Calendar import Calendar;

def main():

    # Create a calendar
    calendar = Calendar()
    
    # Create a calendar based on the csv file
    calendar.from_csv("calendar.csv")

    #Create a ics file from the calendar
    calendar.to_ics("calendar.ics")


if __name__ == "__main__":
    main()
