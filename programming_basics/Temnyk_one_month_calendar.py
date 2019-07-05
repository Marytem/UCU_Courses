def weekdayByNumber(number):
    """
    number : an integer in range [0, 6]
    return : a string representing a weekday
             (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")

    >>> weekdayByNumber(3)
    "thu"
    """
    assert ((number >= 0) and (number <= 6)),\
            "Invalid argument: number out of range"

    if number == 0:
        return "mon"
    if number == 1:
        return "tue"
    if number == 2:
        return "wed"
    if number == 3:
        return "thu"
    if number == 4:
        return "fri"
    if number == 5:
        return "sat"
    if number == 6:
        return "sun"


def getWeekday(date):
    """
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError with corresponding message
    return : an integer representing a weekday(0 represents monday and so on)
    read about algorithm at
    http://vidpo.net/de-znajti-metod-algoritm-viznachennja-dnja-tizhnja.html

    >>> getWeekday("12.08.2015")
    2
    >>> getWeekday("28.02.2016")
    6
    """
    day = int(date.split(".")[0])
    month = int(date.split(".")[1])
    year = int(date.split(".")[2])

    assert(day > 0), "Invalid date: day <= 0"
    assert(month > 0), "Invalid date: month <= 0"
    assert(month <= 12), "Invalid date: month > 12"
    assert(year > 1583), "Invalid date: year <= 1583"

    if (month == 1) or (month == 3) or (month == 5) or (month == 7)\
                    or (month == 8) or(month == 10) or (month == 12):
        assert (day <= 31), "Invalid date: day > 31"
    elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
        assert (day <= 30), "Invalid date: day > 30"
    elif ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        assert (day <= 29), "Invalid date: day > 29"
    else:
        assert (day <= 28), "Invalid date: day > 28"

    if month <= 2:
        day += 3
        year -= 1

    weekdayNumber = (day + year + (year // 4) - (year // 100) +
                     (year // 400) + (31 * month + 10) // 12) % 7
    return weekdayNumber


def getCalendar(month, year):
    """
    month : an integer in range[1 , 12]
    year : an integer (strictly speaking the algorithm in getWeekday works
           correctly only for Gregorian calendar, so year must be greater
           than 1583)
    when arguments are invalid raises AssertionError with corresponding message
    return : a string representing a calendar for given month and year

    >>> get Calendar(8 , 2015)
    The calendar is:
    mon tue wed thu fri sat sun
                        1   2
    3   4   5   6   7   8   9
    10  11  12  13  14  15  16
    17  18  19  20  21  22  23
    24  25  26  27  28  29  30
    31
    """
    assert(month > 0), "Invalid date: month <= 0"
    assert(month <= 12), "Invalid date: month > 12"
    assert(year > 1583), "Invalid date: year <= 1583"

    calendar = []
    for i in range(7):
        calendar.append("")

    for i in range(7):
        calendar[i] += weekdayByNumber(i)

    if (month == 1) or (month == 3) or (month == 5) or (month == 7)\
                    or (month == 8) or(month == 10) or (month == 12):
        numberOfDays = 31
    elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
        numberOfDays = 30
    elif ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        numberOfDays = 29
    else:
        numberOfDays = 28

    firstDay = getWeekday("1." + str(month) + "." + str(year))
    calendarString = ' '

    for i in range(7):
        calendarString += weekdayByNumber(i) + ' '
    calendarString += '\n'

    for i in range(firstDay):
        calendarString += '    '

    dayNum = 1
    for i in range(firstDay, 7):
        calendarString += ' ' + str(dayNum) + '  '
        dayNum += 1
    calendarString += '\n'

    for i in range(7 - firstDay, numberOfDays):
        if dayNum >= 10:
            calendarString += ' ' + str(dayNum) + ' '
        else:
            calendarString += ' ' + str(dayNum) + '  '
        dayNum += 1
        if (firstDay+dayNum-1) % 7 == 0:
            calendarString += '\n'

    return calendarString

try:
    print("Type month")
    month = input()
    month = int(month)
    print("Type year")
    year = input()
    year = int(year)
    print("\n\nThe calendar is: ")
    print(getCalendar(month, year))
except ValueError as err:
    print(err)
