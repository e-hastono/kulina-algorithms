""" Fibonacci Numbers - Kulina

Created by Emmanoel Pratama Putra Hastono

This file allows the user to input an integer that represents the position of a Fibonacci number that
the user wants to know, and prints that number

This script contains the main function fibonacci_number_counter, that takes the position as the
input and returns the Fibonacci number at that position

This code is developed in Python 3.6.4, and cannot be used for Python 2.x without adjustments.

"""
def fibonacci_number_counter(p):
    """Gets the position of a Fibonacci number and returns the Fibonacci number

    Parameters
    ----------
    p : int
        The position of the Fibonacci number that the user wants to know

    Returns
    -------
    int
        The Fibonacci number on that position
    """
    if p == 0:
        return 0
    elif p == 1 or p == 2:
        return 1
    else:
        fibonacci_list = [1, 1]
        while len(fibonacci_list) < p:
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

        return fibonacci_list[-1]

if __name__ == '__main__':
    while True:
        position = int(input("What is the position of the Fibonacci number you are looking for? "))
        if position < 0:
            print("Position is not valid, try again")
            continue
        else:
            fibonacci_number = fibonacci_number_counter(position)
            print("Fibonacci number at position " + str(position) + ' is ' + str(fibonacci_number))
            break