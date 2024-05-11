'''
You are given an array of integers 'ARR' containing N elements. Each integer is in the range [1, N-1], with exactly one element repeated in the array.

Your task is to find the duplicate element. The duplicate element may be repeated more than twice in the error, but there will be exactly one element that is repeated in the array.

Note :

All the integers in the array appear only once except for precisely one integer which appears two or more times.
'''


def findDuplicate(arr: list, n: int):
    # Write your code here.
    # Returns an integer.

    arr.sort()

    i = 0

    while i <= n - 2:
        if arr[i] == arr[i + 1]:
            return arr[i]
        i += 1