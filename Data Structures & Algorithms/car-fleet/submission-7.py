class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=[(p,s)for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        fleets=1
        prevTime=(target-pairs[0][0])/pairs[0][1]
        for i in range(1,len(pairs)):
            currTime=(target-pairs[i][0])/pairs[i][1]
            if prevTime>=currTime:
                continue
            fleets+=1
            prevTime=currTime
        return fleets

