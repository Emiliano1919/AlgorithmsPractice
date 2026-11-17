class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        total=len(A)+len(B)
        half=total//2

        if len(A)>len(B):
            A,B=B,A
        
        L=0
        R=len(A)-1
        while True:
            mA=L+(R-L)//2
            mB=half-(mA+1)-1
            
            Aleft=A[mA] if mA>=0 else float("-infinity")
            Aright=A[mA+1] if mA+1<len(A) else float("infinity")
            Bleft=B[mB] if mB>=0 else float("-infinity")
            Bright=B[mB+1] if mB+1<len(B) else float("infinity")

            if Aleft<=Bright and Bleft<=Aright:
                if total%2:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft)+ min(Aright,Bright))/2
            elif Aleft>Bright:
                R=mA-1
            else:
                L=mA+1