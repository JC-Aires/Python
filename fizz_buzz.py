'''
Name: fizz_buzz.py
Purpose: Fizz Buzz - A program that prints the numbers from 1 to 100.
But for multiples of 3 print “Fizz” instead of the number and for the
multiples of 5 print “Buzz”. For numbers which are multiples of both 3
and 5 print “FizzBuzz”.
Author: JC-Aires
'''

for num in range(1,101):
    # 1st test if num is multiple of both 3 and 5 so the program does
    # not return a false positive without checking the other multiple.
    if num % 3 == 0 and num % 5 == 0:
        print ('FizzBuzz')

    elif num % 3 == 0:
        print ('Fizz')

    elif num % 5 == 0:
        print ('Buzz')

    else:
        print (num)
