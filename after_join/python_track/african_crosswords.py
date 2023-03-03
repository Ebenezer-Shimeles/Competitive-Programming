from collections import defaultdict


n, m = list(map(int, input().split()))


col_set = defaultdict(int)
row_set = defaultdict(int)

grid = []
for i in range(n):
    s = input()
    grid.extend(list(s))
s = len(grid)
#print(grid)
#works find
i = j = 0
for k in range(s):
        if k % m == 0:
          j = 0
          i += 1
        col_set[f'{grid[k]}{j}'] += 1
        row_set[f'{grid[k]}{i}'] += 1
        j += 1
#print(col_set, row_set)
#works find
i = j = 0
for k in range(s):
        
        if k % m == 0:
          j = 0
          i += 1
        key_row = f'{grid[k]}{i}'
        key_column = f'{grid[k]}{j}'
        #3 print(k, i, j )
        if row_set[key_row] > 1 or col_set[key_column] > 1:
            grid[k] = 'D'
        j += 1
      
#print(grid)
output = ""
i = j = 0
for k in range(s):
        if k % m == 0:
          j = 0
          i += 1
        if grid[k] != 'D':
          output += f'{grid[k]}'
print(output)