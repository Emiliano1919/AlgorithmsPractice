class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[0]*len(points) #Remember this
        res=[]
        for i in range(len(points)):
            x2=points[i][0]
            y2=points[i][1]
            distance[i]=((x2)**2 + (y2)**2,points[i]) #We can remove the sqrt we will still preserve the magnitude
        print(distance)
        return self.quickSelect(distance,0,len(distance)-1,k)

    def quickSelect(self, arr, s,e,k):
        n=len(arr)
        left =s
        pivot=arr[e]
        for i in range(s,e):
            if arr[i][0]<pivot[0]:
                tmp=arr[i]
                arr[i]=arr[left]
                arr[left]=tmp
                left+=1
        tmp=arr[left]
        arr[left]=pivot
        arr[e]=tmp
        if k-1==left:
            return [x[1] for x in arr[:k]]
        elif k-1<left:
            return self.quickSelect(arr,s,left-1,k)
        else:
            return self.quickSelect(arr,left+1,e,k)