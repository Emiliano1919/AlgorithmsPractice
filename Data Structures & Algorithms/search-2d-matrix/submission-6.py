class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L=0
        R=len(matrix)*len(matrix[0])-1
        while L<=R:
            mid=L+(R-L)//2
            row=mid//len(matrix[0]) #We only move rows when we are above len(matrix[0])
            col=mid%len(matrix[0])
            then=matrix[row][col]
            if then==target:
                return True
            elif then>target:
                R=mid-1
            else:
                L=mid+1
        return False