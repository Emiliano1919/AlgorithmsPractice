class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(r, c): #Declare first
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
                return
            grid[r][c] = "0"  # This way we don't touch it on the next portion of code
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count
