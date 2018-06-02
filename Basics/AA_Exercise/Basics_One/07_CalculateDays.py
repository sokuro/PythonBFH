"""
    calculate number of days between two dates
"""


from datetime import date

firstDate = date(2018, 6, 2)
lastDate = date(2018, 7, 2)

difference = lastDate - firstDate

print(difference.days)
