"""Lab 7 - Cicrle Lab get radius and do circle calculations.

Author: Luke Schneider
Version: 09/20/2023
Honor Code: I got help by following along in CS-149 Lecture
"""

import math


def print_greeting():
    """Print Greeting."""
    print('Welcome to the CS149 Circle Calculator')
    print('')
    print('This application will calculate the area of a circle and/or volume of a sphere.')
    print("")


def enter_radius():
    """
    enter_radius - print a prompt and collect user radius


    Returns:
        float: radius value
    """
    r = float(input('Enter the radius: '))
    return r


def calculate_area(r):
    """
    calculate_area - return area of a circle given radius r
    
    Args:
        r(float): radius of circle
 
    Returns:
        float: area of the circle
    """
    area = math.pi * math.pow(r, 2)
    return area


def calculate_volume(r):
    """
    Args:
        r(float): radius of sphere
    
    Returns:
        float: area of the sphere

    """
    volume = (4/3) * math.pow(r, 3)
    return volume