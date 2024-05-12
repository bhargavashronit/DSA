'''
You are given an array of size ‘N’. The elements of the array are in the range from 1 to ‘N’.

Ideally, the array should contain elements from 1 to ‘N’. But due to some miscalculations, there is a number R in the range [1, N] which appears in the array twice and another number M in the range [1, N] which is missing from the array.

Your task is to find the missing number (M) and the repeating number (R).

For example:
Consider an array of size six. The elements of the array are { 6, 4, 3, 5, 5, 1 }.
The array should contain elements from one to six. Here, 2 is not present and 5 is occurring twice. Thus, 2 is the missing number (M) and 5 is the repeating number (R).
Follow Up
Can you do this in linear time and constant additional space?
'''


class Solution:

    def missing_and_repeating_number(self, arr):

        n = len(arr)

        sum_n = (n*(n+1))//2

        actual_sum = 0
        repeat = 0

        for i in arr:
            actual_sum += i

        for i in range(len(arr)):

            if (arr[abs(arr[i])-1] < 0):
                repeat = abs(arr[i])
                break

            arr[abs(arr[i])-1] = arr[abs(arr[i])-1] * -1


        missing = sum_n + repeat - actual_sum

        return (missing, repeat)


if __name__ == "__main__":

    print(Solution().missing_and_repeating_number([6,4,3,5,5,1]))