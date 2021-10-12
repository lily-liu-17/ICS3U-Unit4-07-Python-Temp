#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program will convert °C to °F


def fahrenheit():
    user_temp = input("Enter a temperature (°C) : ")
    try:
        user_temp = int(user_temp)
        f_temp = (9 / 5) * user_temp + 32
        print("{0}°C is equal to {1}°F".format(user_temp, f_temp))
    except (Exception):
        print("Invalid input")


def main():
    # call functions
    fahrenheit()

    print("\nDone.")


if __name__ == "__main__":
    main()
