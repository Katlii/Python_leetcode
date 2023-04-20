class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        pos = [[i] for i in range(n)]
        result = [-1] * n
        for r in range(m):
            nxt_pos = [[] for i in range(n)]
            for c, balls in enumerate(pos):
                if not balls: continue
                if c < n - 1 and grid[r][c] == grid[r][c+1] == 1:
                    nxt_pos[c+1] += balls
                elif c > 0 and grid[r][c] == grid[r][c-1] == -1:
                    nxt_pos[c-1] += balls
            pos = nxt_pos
        for c, balls in enumerate(pos):
            for ball in balls:
                result[ball] = c
        return result

grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
print(Solution().findBall(grid))
