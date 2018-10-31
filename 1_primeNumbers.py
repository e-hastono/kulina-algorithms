""" Prime Numbers - Kulina

Created by Emmanoel Pratama Putra Hastono

This file allows the user to input an integer that represents the position of a prime number that
the user wants to know, and prints that number

This script contains the main function prime_number_calculator, that takes the position as the
input and returns the prime number at that position

This code is developed in Python 3.6.4, and cannot be used for Python 2.x without adjustments.

"""
def prime_number_calculator(p):
    """Gets the position of a prime number and returns the prime number

    Parameters
    ----------
    p : int
        The position of the prime number that the user wants to know

    Returns
    -------
    int
        The prime number on that position
    """    
    prime_list = [2]    
    num_test = 3
    
    while len(prime_list) < p:
        for i in prime_list:
            if num_test % i == 0:
                break
        else:
            prime_list.append(num_test)

        num_test += 2

    return prime_list[-1]

if __name__ == '__main__':
    while True:
        position = int(input("What is the position of the prime number you are looking for? "))
        if position < 1:
            print("Position is not valid, try again")
            continue
        else:
            prime_number = prime_number_calculator(position)
            print("Prime number at position " + str(position) + ' is ' + str(prime_number))
            break