class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS= len(grid), len(grid[0])
        maxi=0
        def dfs(r,c):
            nonlocal maxi
            nonlocal cmax
            if min(r,c)<0 or r==ROWS or c==COLS or grid[r][c]!=1:
                return
            cmax+=1
            if cmax>=maxi:
                maxi=cmax
            grid[r][c]=0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    cmax=0
                    dfs(r,c)
        return maxi
