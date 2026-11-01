class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L=0
        R=len(matrix)*len(matrix[0])-1
        while L<=R:
            mid=L+(R-L)//2
            curr= matrix[mid//len(matrix[0])][mid%len(matrix[0])]
            if curr==target:
                return True
            elif curr>target:
                R=mid-1
            else:
                L=mid+1
        return False