class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        # Instead of checking everytime we just build an array
        one_rows = []
        one_columns = []

        zero_rows = []
        zero_column = []

        for i in range(m):
            zero_count = 0
            one_count = 0
            for j in range(n):
                if grid[i][j] == 0:
                    zero_count += 1
                elif grid[i][j] == 1:
                    one_count += 1
            one_rows.append(one_count)
            zero_rows.append(zero_count)
        print(one_rows, ' ', zero_rows)
        for i in range(n):
            zero_count = 0
            one_count = 0
            for j in range(m):
                if grid[j][i] == 0:
                    zero_count += 1
                elif grid[j][i] == 1:
                    one_count += 1
            one_columns.append(one_count)
            zero_column.append(zero_count)
        print(one_columns, ' ', zero_column)
        result = []
        for i in range(m):
            r = []
            for j in range(n):
                r.append(one_rows[i] + one_columns[j] - zero_rows[i] - zero_column[j])
            result.append(r)
        return result

                    