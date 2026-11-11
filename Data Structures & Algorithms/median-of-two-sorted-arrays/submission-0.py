class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1,nums2
        total=len(nums1)+len(nums2)
        half = total//2

        if len(B)<len(A):
            A,B=B,A
        
        L,R=0,len(A)-1

        while True:
            midA=L+(R-L)//2
            midB=half-midA-2 #I don't get the -2

            Aleft= A[midA] if midA >=0 else float("-infinity")
            Aright=A[midA+1] if (midA+1)<len(A) else float("infinity")
            Bleft= B[midB] if midB>=0 else float("-infinity")
            Bright=B[midB+1] if (midB+1)<len(B) else float("infinity")
            if Aleft<=Bright and Bleft <=Aright:
                if total%2:
                    return min(Aright, Bright)
                return (max(Aleft,Bleft)+ min(Aright,Bright))/2
            elif Aleft >Bright:
                R=midA-1
            else:
                L=midA+1
