# CSV to ics converter
This is a simple python script that converts a CSV file to an ics file. The CSV file should have the following columns:

- `Subject`: The subject of the event
- `Start Date`: The start date of the event in the format `YYYY-MM-DD`
- `Start Time`: The start time of the event in the format `HH:MM`
- `End Date`: The end date of the event in the format `YYYY-MM-DD`
- `End Time`: The end time of the event in the format `HH:MM`
- `Description`: The description of the event
- `Location`: The location of the event
- `All Day Event`: Whether the event is an all day event or not (True/False)

The script will read the CSV file and create an ics file with the events.