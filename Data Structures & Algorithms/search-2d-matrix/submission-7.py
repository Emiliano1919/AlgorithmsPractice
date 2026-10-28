class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L=0
        R=len(matrix)*len(matrix[0])-1
        while L<=R:
            mid=L+(R-L)//2
            row=mid//len(matrix[0]) #the size of the row
            col=mid%len(matrix[0])
            suspect=matrix[row][col]
            if suspect==target:
                return True
            elif suspect>target:
                R=mid-1
            else:
                L=mid+1
        return False