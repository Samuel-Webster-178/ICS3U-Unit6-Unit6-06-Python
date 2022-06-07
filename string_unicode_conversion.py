#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


import unicode


def convert_to_unicode(string):
    unicode_string = []
    for counter1 in range(len(string)):
        for key, value in unicode.dictionary.items():
            if string[counter1] == key:
                unicode_string.append(value)
    return unicode_string


def main():
    # I calculate circumference

    # input
    string = input("Enter your string: ")

    # process
    unicode_string = convert_to_unicode(string)

    # output
    print("{0} in hex is {1}".format(string, unicode_string))
    print("\nDone.")


if __name__ == "__main__":
    main()
