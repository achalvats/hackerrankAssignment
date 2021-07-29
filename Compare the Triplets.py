#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ScoreA = 0
    ScoreB = 0
    #print("0")
    for i, j in zip(a, b):
        #print(i, j)
        if (0 < i < 101) and (0 < j < 101):
            #print("1")
            if i > j:
                ScoreA += 1
            elif j > i:
                ScoreB += 1
            else:
                pass

    score = [ScoreA, ScoreB]

    return score


if __name__ == '__main__':
    #fptr = open(os.environ["C:\Users\acvats\Desktop\open this\achal\code\HackerRank\python"], 'w')

    a = list(map(int, input().rstrip().split()))
    #a =[1,2,3]
    b = list(map(int, input().rstrip().split()))
    #b =[1,2,3]
    result = compareTriplets(a, b)
    print(result)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
