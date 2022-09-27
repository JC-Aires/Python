"""
Name: RomanToIntConversion.py
Purpose: Enter a roman number and have the program generate its int equivalent.
Author: JC-Aires
"""


def romanToInt(s):

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9,
              'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}  # All possible roman numbers combinations
    i = 0
    num = 0

    while i < len(s):
        # checks if a valid pair of numbers is in the values list
        if i + 1 < len(s) and s[i:i + 2] in values:
            num += values[s[i:i + 2]]
            i += 2  # increments by 2 as a valid pair means 2 entries
        else:
            num += values[s[i]]
            i += 1
    return num


def main():  # Wrapper function

    prompt = "\nConverting a Roman number to its respective Integer."
    prompt += "\nEnter the desired Roman number: "

    n = input(prompt).upper()
    result = romanToInt(n)

    print(result)


if __name__ == '__main__':
    main()
