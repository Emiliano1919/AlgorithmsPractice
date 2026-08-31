class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        L=R=0
        res=[]
        #We want a monotonic decreasing stack
        while R in range(len(nums)):
            
            while q and nums[R]>=nums[q[-1]]: #To add safely mantain the monotonic stack
                q.pop()
            #The previous while loop assures you the biggest is at the front
            #We can add safely to the back
            q.append(R)
            if q[0]<L: #If the max has expired
                q.popleft()
            if  R-L+1==k:
                res.append(nums[q[0]])
                L+=1
            R+=1
        return res