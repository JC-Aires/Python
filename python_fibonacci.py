'''
Name: python_fibonacci.py
Purpose: Enter a number and have the program generate the Fibonacci sequence to that number.
Author: JC-Aires
'''

def gen_fibon(n):  # Generates a fibonacci sequence with the size of n

    # Set the initial sequence values
    a = 0
    b = 1

    # Calculate the sequence
    for i in range(n):
        yield a # To iterate over a sequence without storing the entire sequence in memory.
        a , b = b , a + b

def main():  # Wrapper function

    # User number of entries input
    prompt = "\nCalculating the Fibonacci sequence."
    prompt += "\nEnter the desired number of entries (n > 0): "
    
    n = int(input(prompt))

    # Processing the sequence
    for num in gen_fibon(n):
        print(str(num) + ' ', end = "") # Format the printing to keep numbers (converted to strings) in the same line

if __name__ == '__main__':
    main()








