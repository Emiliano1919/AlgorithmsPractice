class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[0]*9
        cols=[0]*9
        square=[0]*9
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                val=int(board[r][c])-1
                decal= (1<<val)
                if decal & rows[r]:
                    return False
                if decal & cols[c]:
                    return False
                if decal & square[(r//3)*3+(c//3)]:
                    return False
                rows[r]|=decal
                cols[c]|=decal
                square[(r//3)*3+(c//3)]|=decal
        return True