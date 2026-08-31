class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        q=deque()
        L=0
        for R in range(len(nums)):
            # Remove indices that are outside the window
            if q and q[0] < L:
                q.popleft()

            # Maintain decreasing order from LEFT -> RIGHT
            while q and nums[R] >= nums[q[-1]]:
                q.pop()

            q.append(R)

            # Window is complete
            if R - L + 1 == k:
                res.append(nums[q[0]])
                L += 1

        return res


