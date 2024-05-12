'''
For a given integer array/list 'ARR' of size 'N' containing all distinct values, find the total number of 'Inversions' that may exist.

An inversion is defined for a pair of integers in the array/list when the following two conditions are met.

A pair ('ARR[i]', 'ARR[j]') is said to be an inversion when:

1. 'ARR[i] > 'ARR[j]'
2. 'i' < 'j'

Where 'i' and 'j' denote the indices ranging from [0, 'N').
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= N <= 10^5
1 <= ARR[i] <= 10^9

Where 'ARR[i]' denotes the array element at 'ith' index.

Time Limit: 1 sec
'''

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


# Function to merge the two subarrays.
def merge(arr, left, mid, right):
    i = left
    j = mid
    k = 0
    invCount = 0
    temp = [0 for x in range(right - left + 1)]

    while ((i < mid) and (j <= right)):
        if (arr[i] <= arr[j]):
            temp[k] = arr[i]
            k += 1
            i += 1

        else:
            temp[k] = arr[j]
            invCount += (mid - i)
            k += 1
            j += 1

    while (i < mid):
        temp[k] = arr[i]
        k += 1
        i += 1

    while (j <= right):
        temp[k] = arr[j]
        k += 1
        j += 1

    k = 0
    for i in range(left, right + 1):
        arr[i] = temp[k]
        k += 1
    print(temp)
    print(arr)
    return invCount


# Function to split two subarrays and then merge them and count inversions.
def mergeSort(arr, left, right):
    invCount = 0

    if (right > left):
        mid = (right + left) // 2

        """
            Divide the array into two parts
            total inversion count will be the
            sum of 'INVCOUNT' of left part +
            'INVCOUNT' of right part + 'INVCOUNT' of
            their combined part.
        """
        invCount = mergeSort(arr, left, mid)
        invCount += mergeSort(arr, mid + 1, right)

        # Merge both parts and count their combined inversions.
        invCount += merge(arr, left, mid + 1, right)

    return invCount


def getInversions(arr, n):
    return mergeSort(arr, 0, n - 1)

if __name__ == "__main__":

    print(getInversions([2, 5, 1, 3, 4], 5))