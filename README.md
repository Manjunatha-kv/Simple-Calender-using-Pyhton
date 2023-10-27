# Simple-Calender-using-Pyhton
Python script that uses the calendar module to generate and print a calendar for a specified year.
Here's how the code works:

It imports the calendar module, which provides functionality to work with calendars.

It prompts the user to enter a year, and the input is stored in the variable year.

It creates a TextCalendar object called cal with Sunday as the first day of the week. This means that the calendar will start each week with Sunday as the first day of the week.

It iterates through each month (from January to December) using a for loop with the month variable ranging from 1 to 12.

For each month, it uses the cal.formatmonth(year, month) function to generate and print a calendar for that month of the specified year.


