"""Circle Driver test driver for the circle_play class.

Author: Nancy Harris - modified by Alvin Chao
Version: 09/23/2015, 1-28-22
"""
import sys
import circle_play

if __name__ == "__main__":
    problem = 0
    args = (sys.argv)

    fVals = [1.0, 5.0, 10.5]
    if (len(args) > 1):
         problem = int(args[1])
    else:
         problem = 0
    if (problem >= 0):
         print("Testing Greeting")
         circle_play.print_greeting();
    if (problem == 0 or problem >= 2):
        print("Testing Input");
        for i in range(0, len(fVals)):
            fVals[i] = circle_play.enter_radius();
        print("The values you entered were: ")
        for val in fVals:
            print(val,"\t");
    if (problem == 0 or problem == 3):
        for val in fVals:
            print("A circle of radius", val, "has area of",
                  circle_play.calculate_area(val))
    if (problem == 0 or problem == 4):
        for val in fVals:
            print("A sphere of radius", val, "has volume of",
                  circle_play.calculate_volume(val));
