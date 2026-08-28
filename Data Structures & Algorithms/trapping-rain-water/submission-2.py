class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 1
        r = len(height) - 2

        leftMax = height[0]
        rightMax = height[-1]

        res = 0

        while l <= r:

            if leftMax < rightMax:
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
                l += 1

            elif rightMax < leftMax:
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                r -= 1

            else:
                # leftMax == rightMax

                # Process LEFT position
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
                l += 1

                # Process RIGHT position only if it
                # hasn't already been processed
                if l <= r:
                    rightMax = max(rightMax, height[r])
                    res += rightMax - height[r]
                    r -= 1

        return res