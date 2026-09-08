from datetime import datetime, timedelta

today = datetime.now()                         # Get current date and time

print("Today:", today.strftime("%d-%m-%Y"))    # Format the date

future = today + timedelta(days=7)             # Add 7 days

print("After 7 days:", future.strftime("%d-%m-%Y"))

date_string = "01-09-2026"

date = datetime.strptime(date_string, "%d-%m-%Y")  # String → datetime

difference = today - date                       # Find date difference

print("Difference:", difference.days, "days")