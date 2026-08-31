class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque() #Monotonically decreasing
        L=R=0
        res=[]
        while R <len(nums):
            #We eliminate the ones that will never be a maximum so anything small that comes before we found a big one
            while q and nums[R]>=nums[q[-1]]:
                q.pop()
            q.append(R) #It is safe to append to the back as now nums[R]<nums[q[-1]]
            if q[0]<L: #Expired data needs to go
                q.popleft()
            if R-L+1==k:
                res.append(nums[q[0]])
                L+=1
            R+=1
        return res
