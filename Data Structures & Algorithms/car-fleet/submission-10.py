class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=[(p,s)for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        q=[]
        for p,s in pairs:
            c=(target-p)/s
            q.append(c)
            if len(q)>1 and q[-2]>=q[-1]:
                q.pop()
        return len(q)
