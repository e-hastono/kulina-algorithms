""" Number Components - Kulina

Created by Emmanoel Pratama Putra Hastono

This file allows the user to input a number as a string with dots as thousands separators, and
prints each digits with zeros according to their positions.

This script contains the main function number_component, that takes the number and returns
a list of the digits with zeros

This code is developed in Python 3.6.4, and cannot be used for Python 2.x without adjustments.

"""
def number_component(num_string):
    """Gets a number with dot thousands separators and returns the list of digits with zeros

    Parameters
    ----------
    p : str
        The number as a string with dot thousands separators

    Returns
    -------
    list
        The list of integers of the digits with zeros
    """
    number_int = ''.join(num_string.split('.'))
    return [int(number_int[i]) * int(10**(len(number_int)-1-i)) for i in range(len(number_int))]

if __name__ == '__main__':
    number = input("Insert the number (with dots as thousands separators): ")
    
    for item in number_component(number):
        print(item)