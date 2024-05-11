'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.



Example 1:


Input: matrix = v
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

'''


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for i in rows:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0

        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0


if __name__ == "__main__":
    print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))