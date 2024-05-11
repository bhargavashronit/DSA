'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]'''


class Solution:

    def generate(self, numsRows):

        result = []

        for i in range(numsRows):
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row)-1):
                row[j] = result[i-1][j-1] + result[i-1][j]

            result.append(row)

        return result


if __name__ == "__main__":
    print(Solution().generate(5))