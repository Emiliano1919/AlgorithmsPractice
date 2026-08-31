class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        q=deque()
        L=0
        for R in range(len(nums)):
            if q and q[0]<L: #If the left pointer has passed the first of the queue remove it
                q.popleft()

            while q and nums[R]>=nums[q[-1]]: #Add current value to monotonic decreasing queue
                q.pop() #Remove the smaller ones
            if q and nums[R]>=nums[q[0]]:
                q.appendleft(R)
            else:
                q.append(R)
            if R-L+1==k:
                res.append(nums[q[0]])
                L+=1
        return res


