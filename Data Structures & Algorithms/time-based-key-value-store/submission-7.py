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
            M=L+(R-L)//2
            if values[M][0]<=timestamp:
                L=M+1
                res=values[M][1]
            else:
                #values[M]>timestamp
                R=M-1
        return res



