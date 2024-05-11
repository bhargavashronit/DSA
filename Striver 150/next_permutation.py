'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
'''


class Solution:
    def reverse(self, arr, start):
        i, j = start, len(arr)-1
        while i<j:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1

    def next_permutation(self, arr):

        j = len(arr) - 2

        while j >= 0 and arr[j] >= arr[j+1]:
            j-=1


        i = len(arr) -1
        if j >= 0:
            while i >= 0 and arr[i] <= arr[j]:
                i -= 1

            arr[i], arr[j] = arr[j], arr[i]

        self.reverse(arr, j+1)

        print(arr)


if __name__ == "__main__":
    Solution().next_permutation([2,1,3,2])