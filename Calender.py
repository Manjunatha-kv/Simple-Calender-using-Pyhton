import calendar
year = int(input("Enter Year: "))
cal = calendar.TextCalendar (calendar. SUNDAY)
for month in range(1, 13):
    print(cal.formatmonth (year, month))