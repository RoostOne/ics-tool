# CSV to ics converter
## A python program to convert a CSV file to an ics file
This program is a simple python program that converts a CSV file to an ics file. It is using the datetime package to handle the dates and times. 

The CSV file should have the following columns:
| Date | Time | Title | Loacation |
|----------|----------|----------|----------|
|Fr., 10.05.2024|15:15 - 17:45 Uhr|Event 1|office|
|Mo., 13.05.2024|18 - 22 Uhr|Event 2|office|
|Di., 14.05.2024|16 - 22 Uhr|Event 3|office|

The program will read the CSV file and create an ics file with the events. The ics file can be imported into a calendar application like Google Calendar, Outlook, etc.

## How to use   
1. Clone the repository
2. Install the required packages with `pip install -r requirements.txt`
3. Create a CSV file with the events named `calendar.csv`
4. run the main.py file with `python main.py`

## Future Goals
- Create a CLI interface or online tool
- Support for more date and time formats
