class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        summ=0
        for i in range(n):
            for j in range(m):
                summ+=self.find(grid, i, j, n, m)
        return summ
    def find(self, grid, i, j, n, m):
        if 0<=i<n and 0<=j<m:
            if grid[i][j]=='1':
                grid[i][j]='0'
                self.find(grid, i+1, j, n,m)
                self.find(grid, i, j-1, n,m)
                self.find(grid, i-1, j, n,m)
                self.find(grid, i, j+1, n,m)
                return 1
        return 0
        


grid=[['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
out=Solution().numIslands(grid)
print(out)


