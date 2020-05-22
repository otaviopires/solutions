class Solution:
    
    def biggestTable(self, grid):
        collumns = len(grid)
        result_collumn = []
        for i in range(collumns):
            collumn = [row[i] for row in grid]
                        

        # return isRectangle(grid)


def get_matrix():
    row = int(input())
    col = int(input())
    grid = [["0"]*col]*row

    for i in range(row):
        line = input()
        grid[i] = list(line)[0:col]
    return grid


def isRectangle(grid): 
    rows = len(grid) 
    print('rows:'+str(rows))
    if (rows == 0): 
        return False
  
    columns = len(grid[0]) 
    table = {} 

    for i in range(rows):  
        for j in range(columns - 1): 
            for k in range(j + 1, columns):  
                if (grid[i][j] == 1 and
                    grid[i][k] == 1): 
  
                    if (j in table and k in table[j]): 
                        return True
  
                    if (k in table and j in table[k]): 
                        return True
  
                    if j not in table: 
                        table[j] = set() 
                    if k not in table: 
                        table[k] = set() 
                    table[j].add(k)  
                    table[k].add(j) 
    return False    


if __name__ == "__main__":
    sol = Solution()
    # grid = get_matrix()
    grid = [[1,1,1,1,0], 
            [1,1,0,1,0], 
            [1,1,0,0,0], 
            [0,0,0,0,0]]
    expect1 = 6

    grid2 = [[1, 0, 1, 1, 1],
    	    [1, 0, 1, 1, 1],
	        [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0]]
    expect2 = 9

    grid3 = [[1,0,1,0,0],
            [1,0,1,1,1,],
            [1,1,1,1,1],
            [1,0,0,1,0]]
    expect3 = 6

    bigTable = sol.biggestTable(grid)
    print("test 1 result: "+str(bigTable))
    print('expected 1: '+str(expect1))

    bigTable = sol.biggestTable(grid2)
    print("test 2 result: "+str(bigTable))
    print('expected 2: '+str(expect2))

    bigTable = sol.biggestTable(grid3)
    print("test 3 result: "+str(bigTable))
    print('expected 3: '+str(expect3))
