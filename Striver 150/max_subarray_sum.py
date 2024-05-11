'''
You are given an array 'arr' of length 'n', consisting of integers.



A subarray is a contiguous segment of an array. In other words, a subarray can be formed by removing 0 or more integers from the beginning and 0 or more integers from the end of an array.



Find the sum of the subarray (including empty subarray) having maximum sum among all subarrays.



The sum of an empty subarray is 0.



Example :
Input: 'arr' = [1, 2, 7, -4, 3, 2, -10, 9, 1]

'''


class Solution:
    def maxSubArray(self, nums):

        max_sum = -99999999
        curr_sum = 0

        i = 0
        while i < len(nums):
            curr_sum += nums[i]

            if curr_sum > max_sum:
                max_sum = curr_sum

            if curr_sum < 0:
                curr_sum = 0

            i += 1
        return max_sum

