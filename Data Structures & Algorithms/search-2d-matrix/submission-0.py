class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        L=0
        R=m*n-1
        while L<=R:
            mid= L+(R-L)//2
            row=mid//m
            col=mid%m
            if matrix[row][col]<target:
                L=mid+1
            elif matrix[row][col]>target:
                R=mid-1
            else:
                return True
        return False
                

            
