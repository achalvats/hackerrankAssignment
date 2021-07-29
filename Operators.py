#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import localcontext, Decimal, ROUND_HALF_UP


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    return meal_cost + round(((tip_percent / 100) * meal_cost), 2) + round(((tax_percent / 100) * meal_cost), 2)


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    total_cost = solve(meal_cost, tip_percent, tax_percent)
    with localcontext() as ctx:
        ctx.rounding = ROUND_HALF_UP
        print(Decimal(total_cost).to_integral_value())
        # print(round(total_cost))
