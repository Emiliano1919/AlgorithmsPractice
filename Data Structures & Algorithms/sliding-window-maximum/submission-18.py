class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        L=R=0
        res=[]
        while R !=len(nums):
            while q and nums[R]>nums[q[-1]]:
                q.pop()
            q.append(R)

            while L>q[0]:
                q.popleft()
            if R+1>=k:
               res.append(nums[q[0]])
               L+=1
            R+=1
        return res