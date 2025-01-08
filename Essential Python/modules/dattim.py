#It helps us create, format and manipulate dates and times effortlessly
import datetime

#Getting the current date and time
current_datetime = datetime.datetime.now()
print("Current datetime", current_datetime, sep=":")

#Formatting a datetime object as a string
formatted_date = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted date", formatted_date, sep=":")

#Creating a datetime object from a string
date_string = "2024-11-15"
converted_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print("Converted date", converted_date, sep=":")

#Calculating the difference between two dates
date1 = datetime.datetime(2024, 5, 8)
date2 = datetime.datetime(2024, 9, 12)
date_difference = date2 - date1
print("Difference between the two dates", date_difference, sep=":")

#Getting the current date
current_date = datetime.date.today()
print("Current date", current_date, sep=":")

#Calculating the difference between two datetime objects
timedelta = datetime.timedelta(days=7)
future_date = current_date + timedelta
print("Future date (7 days from now)", future_date, sep=":")

#Get the day of the week
day_of_week = current_date.strftime("%A")
print("Today is", day_of_week, sep=":")