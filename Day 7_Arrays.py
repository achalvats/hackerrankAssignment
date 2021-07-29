#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    #
    # arr_rev = ''
    # for i in reversed(range(n)):
    #     arr_rev += str(arr[i])
    #     arr_rev += " "
    #
    # print(arr_rev)
    #
    print(*reversed(arr))
#print(' '.join(map(str, reversed(arr))))

