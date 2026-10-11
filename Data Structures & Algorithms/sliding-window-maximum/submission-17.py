class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        L=R=0
        while R <len(nums):
            while q and nums[q[-1]]<nums[R]:
                #We found something bigger so we pop until we have something that's not bigger
                q.pop()
            q.append(R)#Because we ensured ourselves something bigger is going to enter we can append
            if L>q[0]:
                #If the top expired then remove it
                q.popleft()
            if (R+1)>=k:
                res.append(nums[q[0]])
                L+=1
            R+=1
        return  res
            