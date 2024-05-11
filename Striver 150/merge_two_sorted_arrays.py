'''
Ninja has been given two sorted integer arrays/lists ‘ARR1’ and ‘ARR2’ of size ‘M’ and ‘N’. Ninja has to merge these sorted arrays/lists into ‘ARR1’ as one sorted array. You may have to assume that ‘ARR1’ has a size equal to ‘M’ + ‘N’ such that ‘ARR1’ has enough space to add all the elements of ‘ARR2’ in ‘ARR1’.

For example:

‘ARR1’ = [3 6 9 0 0]
‘ARR2’ = [4 10]
After merging the ‘ARR1’ and ‘ARR2’ in ‘ARR1’.
‘ARR1’ = [3 4 6 9 10]
'''

class Solution:

    def merge_two_sorted_arrays(self, arr1, arr2):
            i = len(arr1) - len(arr2) - 1
            j = len(arr2) - 1

            to_insert = len(arr1) - 1

            while i >= 0 and j >= 0:

                if arr1[i] > arr2[j]:
                    arr1[to_insert] = arr1[i]
                    i -= 1
                    to_insert -= 1
                else:
                    arr1[to_insert] = arr2[j]
                    j -= 1
                    to_insert -= 1

            while i >= 0 and to_insert >= 0:
                arr1[to_insert] = arr1[i]
                i -= 1
                to_insert -= 1

            while j >= 0 and to_insert >= 0:
                arr1[to_insert] = arr2[j]
                j -= 1
                to_insert -= 1
            return arr1

if __name__ == "__main__":
    print(Solution().merge_two_sorted_arrays([3, 6, 9, 0, 0], [4,10]))