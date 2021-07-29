#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the factorial function below.
def factorial(n):
    return n*factorial(n-1) if n >1 else 1



    # factorial = lambda x: 1 if x <= 1 else x * factorial(x - 1)
    # print(factorial(int(input())))
    #

    # fact = 1
    # while (n != 1):
    #     fact *= n
    #     n = n - 1
    #
    # return fact


if __name__ == '__main__':
    n = int(input())

    result = factorial(n)
    print(result)

