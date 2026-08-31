class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        L=R=0
        res=[]
        while R in range(len(nums)):
            while q and nums[R]>nums[q[-1]]: #If useless smaller delete from back
                q.pop()
            if q and nums[R]>nums[q[0]]:
                print('Running this')
                q[0]=1001
            else:
                q.append(R)
            if q[0]<L: # If expired delete the expired big
                q.popleft()
            if R-L+1==k: #If valid you add it to result then you move the Left pointer
                res.append(nums[q[0]])
                L+=1
            R+=1
            
        return res