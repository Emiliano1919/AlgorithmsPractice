class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(int)
        cols=defaultdict(int)
        squares=defaultdict(int)
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                val=int(board[r][c])-1
                decal=(1<<val)
                if decal & rows[r]:
                    return False
                if decal & cols[c]:
                    return False
                if decal & squares[(r//3)*3+(c//3)]:
                    return False
                rows[r]|=decal
                cols[c]|=decal
                squares[(r//3)*3+(c//3)]|=decal
        return True