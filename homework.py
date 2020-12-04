#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a progame claculate bonus money.

import constants


def main():
    # This is the function claculate bonus money.

    # Input
    money = int(input("Enter the money you earn for a year:"))
    length_of_service = int(input("Enter the length of service year:"))
    print("")

    # Process
    bonus_money = money * constants.bonus

    # output
    if length_of_service > 5:
        print("Your bonus money for this year is ${}".format(bonus_money))
    else:
        print("Sorry, you will not have bonus money for this year.")


if __name__ == "__main__":
    main()
