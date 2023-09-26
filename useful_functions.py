""" 
This module contains useful functions that can be used in other modules.
written by : Joe Defendre 
version: 1.0
date: 2023
"""

def multiply_two_numbers(num1: int, num2: int) -> int:
    """ 
    this is the multiply_two_numbers function
    :param num1: int
    :param num2: int
    :return: int
    """
    product = num1 * num2
    return product


def print_1_to_10():
    """
    this is the print_1_to_10 function
    :return: None
    """
    for i in range(1,11):
        print(i)
