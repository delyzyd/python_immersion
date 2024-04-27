"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""

from datetime import datetime
from sys import argv

def date_validate(date_text: str) -> bool:
    try:
        value = datetime.strptime(date_text, "%d.%m.%Y").date()
        return True
    except ValueError:
        return False

def _leap_info(date_text: str) -> bool:
    year = int(date_text.split(".")[-1])
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    if len(argv) >= 3:
        date_arg = argv[2]
        if date_validate(date_arg):
            print(f"Date {date_arg} is valid.")
            if _leap_info(date_arg):
                print(f"Year {date_arg.split('.')[-1]} is a leap year.")
            else:
                print(f"Year {date_arg.split('.')[-1]} is not a leap year.")
        else:
            print(f"Date {date_arg} is invalid. Please provide a valid date in format DD.MM.YYYY.")
    else:
        print("Please provide a date argument in the format DD.MM.YYYY.")