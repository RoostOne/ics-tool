from datetime import datetime

# Define the input time string
time_str = "Fr., 10.05.2024;15:15 - 17:45 Uhr"

# Define the input time string
time_str = "Fr., 10.05.2024;15:15 - 17:45 Uhr"

# Remove the "Uhr" from the end of the string
time_str = time_str.replace(" Uhr", "")

# Remove the weekday from the beginning of the string
time_str = time_str.split(",")[1].replace(" ", "")

# Get the date
date = datetime.strptime(time_str.split(";")[0], "%d.%m.%Y")

# Get the start and end time
start_time, end_time = time_str.split(";")[1].split("-")

# Get the start and end time as datetime objects
start_time = datetime.strptime(start_time, "%H:%M")
end_time = datetime.strptime(end_time, "%H:%M")

# Combine the date with the start and end time
start_time = datetime.combine(date, start_time.time())
end_time = datetime.combine(date, end_time.time())

# Print the results
print(end_time)