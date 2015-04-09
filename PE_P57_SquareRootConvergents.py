## Author: James Norcross
## Date: 4/08/15
## Purpose: Solve Project Euler Problem 57
## Description: finds nth expansion of continued fraction representation
## of the square root of two for n between 1 and 1000.  Counts the number
## of times that the nth expansion has more digits in its numerator than
## its denominator

import sys
sys.setrecursionlimit(1100)

from math import log10

## recursive function to find the nth term to be added to 1 in
## the expansion for the square root of 2
## n integer order of delta
## delta a tuple representing a fraction
def findDelta(n, delta):
    if (n == 1):
        return (1,2)
    else:
        ## new_delta = 1/(2+ findDelta(n-1, delta)
        denom = fractionSum((2,1), findDelta(n-1, delta))
        return fractionInverse(denom)

## returns the fractional sum (non reduced) of two fractions a and b
## a, b and sum tuples representing fractions
def fractionSum(a, b):
    num = a[0] * b[1] + a[1] * b[0]
    denom = a[1] * b[1]
    return (num, denom)

## returns a tuple representing the inverse of a where a
## is a tuple representing a fraction
def fractionInverse(a):
    return (a[1], a[0])


count = 0

for n in range(1,1001):
    result = fractionSum((1,1), findDelta(n, (0,0)))
    if (int(log10(result[0])) > int(log10(result[1]))):
        count += 1

print count
