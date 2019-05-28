"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
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

args = sys.argv[1:]
def cal(month=None, year=None, *args):
  if(month != None):
    month = int(month)
    if(year == None):
      year = int(datetime.today().strftime("%Y"))
    else:
      year = int(year)
    print(calendar.monthcalendar(year, month))
  else:
    month = int(datetime.today().strftime("%m"))
    year = int(datetime.today().strftime("%Y"))
    print(calendar.monthcalendar(year, month))
    print('Usage: py 14_cal.py month [year]')

cal(*args)
