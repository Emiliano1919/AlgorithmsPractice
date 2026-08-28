class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res=[]
        L=0
        currTotal=0
        curr=deque()
        for R in range(len(arr)):
            if R-L+1>k:
                currTotal-=curr.popleft()
                L+=1
            curr.append(arr[R])
            currTotal+=arr[R]
            if currTotal/k>=threshold and len(curr)==k:
                res.append(list(curr))
        return len(res)
                

        