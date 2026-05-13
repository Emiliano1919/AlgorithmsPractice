class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[0]*len(points) #Remember this
        res=[]
        for i in range(len(points)):
            x1=0
            y1=0
            x2=points[i][0]
            y2=points[i][1]
            distance[i]=((x2)**2 + (y2)**2,points[i]) #We can remove the sqrt we will still preserve the magnitude
        distance.sort() #It will sort lexicoprahically using the first and second part if the first is the same
        for i in range(k):
            res.append(distance[i][1])
        return res