"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

month_year = input("Enter a month and a year: ").replace(" ", "").split(",")

def create_calender(*args):
    # Instantiates class
    date = datetime.today()
    rendered_calendar = calendar.TextCalendar()
    # Gets current year
    year = date.year
    if args[0] == '':
        print("Please enter two numbers. The first number should be a number between 1-12 to represent a month. The second number should be four digits representing a year. A comma must be in-between each number.")
    elif len(args) == 2:
        rendered_calendar.prmonth(int(args[1]), int(args[0]))
    elif len(args) == 1:
        rendered_calendar.prmonth(year, int(args[0]))


create_calender(*month_year)