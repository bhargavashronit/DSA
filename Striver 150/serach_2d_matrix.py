
'''
Problem statement
You have been given a 2-D array 'mat' of size 'M x N' where 'M' and 'N' denote the number of rows and columns, respectively. The elements of each row are sorted in non-decreasing order.



Moreover, the first element of a row is greater than the last element of the previous row (if it exists).



You are given an integer ‘target’, and your task is to find if it exists in the given 'mat' or not.



Example:
Input: ‘M’ = 3, 'N' = 4, ‘mat’ = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ‘target’ = 8

Output: true

Explanation: The output should be true as '8' exists in the matrix.
'''

def searchMatrix(mat, target):
    # Write your code here.
    i = 0
    j = (len(mat[0])) - 1

    while i < len(mat) and j >=0:

        if mat[i][j] == target:
            return True
        if mat[i][j] < target:
            i+=1
        else:
            j-=1

    return False


if __name__ == "__main__":

    print(searchMatrix([[1,2,3,4], [5,6,7,8], [9,10,11,12]], 8))