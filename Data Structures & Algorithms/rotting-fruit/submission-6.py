class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        rottenLocations=deque()
        counterFresh,steps=0,0
        totalSteps=-1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    counterFresh+=1
                if grid[r][c]==2:
                    rottenLocations.append((r,c))
        
        if counterFresh == 0: return 0
        
        neighbors = [[0,1],[0,-1],[1,0],[-1,0]]

        while rottenLocations and counterFresh > 0:
            for _ in range(len(rottenLocations)):
                r, c = rottenLocations.popleft()
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if min(nr,nc) <0 or nr==ROWS or nc==COLS or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2 #Doubts have been resolved, check the conditional above
                    counterFresh -= 1
                    rottenLocations.append((nr, nc))
            steps += 1
        
        return steps if counterFresh == 0 else -1

