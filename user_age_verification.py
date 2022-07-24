"""
Author: Felix
------
Date: 15 - February - 2022
----
Last Modified: 23 - July - 2022
-------------

Suppose we want to write a program that will check if a user is eligible
to use our service basing on user age,
when a user is 18+ years old he is eligible but when he is <18 he is not.
Let's build this program
"""
import datetime
import sys


class CheckDate:
    """
    Creating a class that will check user input date and decide
    whether he is eligible for service or not
    """

    def __init__(self, year, month, day):
        self.month = month
        self.year = year
        self.day = day
        self.date_before = datetime.datetime(2003, 1, 1)

    def compare_date(self) -> bool:
        """
        Checking user input date is valid and eligible
        :return: True if eligible and False if not eligible
        """
        if self.convert_user_date() is not None:
            if self.convert_user_date() < self.date_before:
                return True
            else:
                return False

    def convert_user_date(self):
        """
        Formatting user input in dates
        :return: User date of birth
        """
        return datetime.datetime(self.year, self.month, self.day)


if __name__ == "__main__":
    print("Enter your date of birth to continue: \n")
    print("Enter 0 to quit the program")
    month_1 = int(input("Month: \n"))
    if month_1 == 0:
        print("Quiting the program")
        sys.exit(0)
    elif month_1 > 12:
        print("Month not valid")
        sys.exit(0)
    else:
        day_1 = int(input("Day: \n"))
        year_1 = int(input("Year: \n"))

        date = CheckDate(year_1, month_1, day_1)
        if date.compare_date():
            print("Proceed to the next step you are old enough")
        else:
            sys.exit("You are still young to use our service")
