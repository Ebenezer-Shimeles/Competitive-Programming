t = int(input())



def get_transform(i: int , j:int, n:int):

    return (j, n - 1 - i)


for i in range(t):
    size = int(input())

    grid = []
    for j in range(size):
        l = list(*input().split())
        grid.append(l)
    
    v = 0
    
    t = 0
    for current_transform in range(1, 4):
        t = current_transform
        for i in range(size):
            for j in range(size):
                i_t, j_t = i, j
                for k in range(current_transform):
                    i_t, j_t = get_transform(i_t, j_t, size)
                if grid[i][j] != grid[i_t][j_t]:
                    t = 0
    print(t * 90)