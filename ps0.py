# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#PSet 0

import math

def mathFunc(i, j):
    # Use a breakpoint in the code line below to debug your script.

    nPower = float(i)**float(j)
    nLog = math.log(float(i), 2)

    print("x**y =  " + str(nPower))
    print("log(x) =  " + str(nLog))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = input("Enter number x: ")
    y = input("Enter number y: ")

    mathFunc(x, y)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
