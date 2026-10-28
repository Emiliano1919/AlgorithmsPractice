class TimeMap:

    def __init__(self):
        self.m=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        values=self.m[key]
        if not values:
            return ""
        L=0
        R=len(values)-1
        res=""
        while L<=R:
            mid=L+(R-L)//2
            if values[mid][0]<=timestamp:
                res=values[mid][1]
                L=mid+1
            else:
                R=mid-1
        return res