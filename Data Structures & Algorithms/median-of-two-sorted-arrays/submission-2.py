class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1,nums2
        total = len(nums1)+ len(nums2)
        half=total//2

        if len(B)<len(A):
            A,B = B,A
        l,r=0, len(A)-1
        
        while True:
            mA =l+ (r-l)//2
            #mb is a count
            #half-(ma+1) -1 is a count
            mB=half-mA-2

            Aleft=A[mA] if mA>=0 else float("-infinity")
            Aright=A[mA+1] if (mA+1)<len(A) else float("infinity")
            Bleft=B[mB] if mB>=0 else float("-infinity")
            Bright= B[mB+1] if (mB+1)<len(B) else float("infinity")

            if Aleft <=Bright and Bleft<=Aright:
                if total%2:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft)+ min(Aright,Bright))/2
            elif Aleft>Bright:
                r=mA-1
            else:
                l=mA+1