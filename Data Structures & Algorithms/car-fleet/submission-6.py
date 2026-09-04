class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=[(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True) #We need to sort it by order of position so first the one most advanced
        stack=[]
        for p,s in pairs:
            stack.append((target-p)/s)
            # We only absorb once because if not we are deleting the fleets
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop() #Absorb (-1 )into the fleet (-2)because it will get faster ((target-p)/s) to the target so it will be absorbed by the one that goes before
        return len(stack)