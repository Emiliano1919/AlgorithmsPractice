class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        race=[(p,s) for p,s in zip(position,speed)]
        race.sort(reverse=True)
        stack=[]
        for p,s in race:
            rate=(target-p)/s
            stack.append(rate)
            if len(stack)>=2 and stack[-2]>=stack[-1]:
                stack.pop()
        return len(stack)