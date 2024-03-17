def get_map(n,pos,grid):
    i, j = pos
    rlud = [0,0,0,0]
    map = []
    if i and not grid[i-1][j]: 
        map.append((i-1,j))
        rlud[2] = 1
    if j and not grid[i][j-1]: 
        map.append((i,j-1))
        rlud[1] = 1
    if j+1<n and not grid[i][j+1] : 
        map.append((i,j+1))
        rlud[0] = 1
    if i+1<n and not grid[i+1][j] : 
        map.append((i+1,j))
        rlud[3] = 1
    return map,rlud

def check(grid):
    for row in grid:
        for item in row :
            if not item : return False
    return True

def iter_backtrack(n):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    grid[0][0] = 1
    res = 0
    stack = [((0,0),grid)]
    while (stack) :
        pos, grid = stack.pop(-1)
        if pos[0]==n-1 and pos[1]==n-1:
            if check(grid):
                res = res + 1
        else :
            map, rlud = get_map(n,pos,grid)
            # for row in grid :
            #     for item in row :
            #         print (item,end=" ")
            #     print ()
            # print (pos,rlud)
            if rlud=="0011" or rlud=="1100":
                pass
            else :
                for item in map:
                    x, y = item
                    new_grid = []
                    for row in grid :
                        new_grid.append(row[:])
                    new_grid[x][y] = 1
                    stack.append((item,new_grid))
    print (res)

n = 7
iter_backtrack(n)