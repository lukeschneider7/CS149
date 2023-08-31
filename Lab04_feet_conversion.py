"""Lab 04 - convert feet into miles, furlongs and feet.

:Author - Luke Schneider
:Version - 9-1-23
Attribution: I got help from myself on the calculations
"""

input_feet = int(input("Enter a total number of feet: "))
print()

miles = input_feet // 5280
feet_left = input_feet-miles*5280
furlongs = feet_left//660
feet_left = feet_left-furlongs*660
print(input_feet,"total feet is",
      miles, "mile(s)", furlongs, "furlong(s), and", feet_left, "feet remaining")