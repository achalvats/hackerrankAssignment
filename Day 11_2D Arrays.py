#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    n = 6
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    sum = {}
    for i in range(n):
        for j in range(n):
            # print(arr[i][j])
            try:
                #if arr[i + 2][j] is not None and arr[i][j + 2] is not None:
                sum[str(i) + "," + str(j)] = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][
                        j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            except IndexError:
                pass
                #print("Index error")

    #
    # for element in sum:
    #     print(sum[element])
    # #print(sum)
    #
    # print(max(sum, key= sum.get))
    all_values=sum.values()
    print(max(all_values))