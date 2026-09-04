class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L=0
        rowSize=len(matrix[0])
        R=len(matrix)*rowSize-1
        while L<=R:
            mid=int(L+(R-L)/2)
            row=mid//rowSize
            col=mid%rowSize
            selected=matrix[row][col]
            if selected>target:
                R=mid-1
            elif selected<target:
                L=mid+1
            else:
                return True
        return False
            