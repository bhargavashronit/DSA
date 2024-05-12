'''
You have been given an array/list 'ARR' consisting of 'N' integers. Your task is to find the majority element in the array. If there is no majority element present, print -1.

Note:
A majority element is an element that occurs more than floor('N' / 2) times in the array.
'''


class Solution:

    def findMajorityElement(self, arr, n):
        # Write your code here.
        c = 0
        v = 0

        for i in arr:
            if v == 0:
                c = i

            if c == i:
                v += 1
            else:
                v -= 1

        count = 0
        for i in range(0, n):
            if arr[i] == c:
                count += 1

        if count > n / 2:
            return c

        return -1


if __name__ == "__main__":

    print((Solution().findMajorityElement([2, 3, 9, 2, 2], 5)))
    print((Solution().findMajorityElement([8,5,1,9], 4)))