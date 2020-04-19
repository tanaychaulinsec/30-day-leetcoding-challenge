class Solution:
    def numIslands(self, grid):
        ishland=0
        for row in range(0,len(grid)):
            for col in range(0,len(grid[0])):
                if grid[row][col]=='1':
                    ishland +=1
                    self.dfs(grid,row,col)
        return ishland            
    def dfs(self,grid,row,col):
        if row>=0 and col>=0 and row<len(grid) and col<len(grid[row]):
            if grid[row][col]=='1':
                grid[row][col]='0'
                self.dfs(grid,row+1,col)
                self.dfs(grid,row,col+1)
                self.dfs(grid,row-1,col)
                self.dfs(grid,row,col-1)