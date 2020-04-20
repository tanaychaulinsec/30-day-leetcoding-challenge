class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='1':
                    island_count+=1
                    self.dfs(grid,row,col)
        return island_count            
    def dfs(self,grid,row,col):
        if row>=0 and col>=0 and row<len(grid) and col <len(grid[row]):
            if grid[row][col]=='1':
                grid[row][col]='0'
                self.dfs(grid,row+1,col)
                self.dfs(grid,row,col+1)
                self.dfs(grid,row-1,col)
                self.dfs(grid,row,col-1)