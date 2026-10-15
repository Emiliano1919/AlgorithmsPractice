class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        res = h
        while L <= R:
            mid = L + (R - L) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / mid)
            if totalTime <= h:
                res = mid
                R = mid - 1
            else:
                L = mid + 1
        return res
