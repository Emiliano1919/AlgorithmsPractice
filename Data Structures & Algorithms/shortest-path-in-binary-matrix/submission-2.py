class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid), len(grid[0])
        visit = set()
        queue = deque()
        if grid[0][0]!=0:
            return -1
        queue.append((0,0))
        visit.add((0,0))

        count=1
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r==ROWS-1 and c==COLS-1:
                    return count
                neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
                for dr,dc in neighbors:
                    if min(r+dr,c+dc)<0 or r+dr==ROWS or c+dc==COLS or grid[r+dr][c+dc]==1 or (dr+r,dc+c) in visit:
                        continue
                    queue.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))
            count+=1 #WHY IS THE INCREMENTER HERE? because it goes by layers
        return -1