"""Lab 13 list play.

Author: Luke Schneider
Version: 10-25-23
Acknowledgements: I got the code for this lab in class
"""
import random


def part_one():
    """:part_one.
    
    Returns:
        (str): string output from arrays
    """
    return_str = ""
    int_array = [0, 0, 0, 0, 0, 0]
    for i in range(len(int_array)):
        int_array[i] = -1
    for j in range(0, 6):
        return_str += "array[" + str(j) +"]" + " = "
        return_str += str(int_array[j]) + "\n"
    for k in range(0, len(int_array)):
        int_array[k] = k
    for j in range(0, 6):
        return_str += "array[" + str(j) +"]" + " = "
        return_str += str(int_array[j]) + "\n"
    return return_str
    
    
def dice_roll(seed):
    """Dice Roll - rolls a die and returns face value.

    Args:
        seed(int): seed for random or None for Random number based system time
        
    Returns:
        (int): 1-6 value for a die roll
    """
    if seed is not None:
        random.seed(seed)
    return random.randint(1,6)


def part_two():
    """part_two.

    Returns:
        (str): Strin output from list and dice rolls.
    """
    return_str = ""
    rolls = [0, 0, 0, 0, 0, 0]
    for i in range(25):
        value = dice_roll(i)
        if value > 0 and value <= 6:
            rolls[value - 1] += 1
    for i in range(len(rolls)):
        return_str += str(i+1) + ' was rolled ' + str(rolls[i]) + ' times. \n'
    return return_str
    
  
  
def store_array_values(a1, a2):
    """store array values.
    """
    return_str = ""
    for i in range(len(a1)):
        return_str += str(i) + ' A1 = ' + str(a1[i]) + ' A2 = ' + str(a2[i]) + '\n'
    
    return return_str


def change_array(a1, a2):
    """change array values.
    """
    return_str = ""
    for i in range(len(a1)):
        a2[i] = a1[i]
    a1[0] = 99.0
    a2[5] = 99.0
    return a1, a2

if __name__ == '__main__':
    print(part_one())
    print('Array Play')
    print(part_two())
    
    print("Before")
    a1 = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    a2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    print(a1, a2)
    print(store_array_values(a1, a2))
    change_array(a1, a2)
    print("After")
    print(store_array_values(a1, a2))
    a1 = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    a2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    print(store_array_values(a1, a2))
    change_array(a1, a2)
    print("After")
    print(store_array_values(a1, a2))
    a1 = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    a2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    print(store_array_values(a1, a2))
    change_array(a1, a2)
    print("After")
    print(store_array_values(a1, a2))