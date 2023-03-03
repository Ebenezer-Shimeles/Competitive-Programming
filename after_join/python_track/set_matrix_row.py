from collections import defaultdict

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        cols = defaultdict(int)
        rows = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    cols[j] = 1
                    rows[i] = 1

        print(f'cols {cols} rows {rows}')
        for i in range(m):
            for j in range(n):
                if cols[j] or rows[i]:
                    matrix[i][j] = 0
                   
           