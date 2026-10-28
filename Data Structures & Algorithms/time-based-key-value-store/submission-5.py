import bisect
class TimeMap:

    def __init__(self):
        self.m=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        timestamps=self.m[key]
        if not timestamps:
            return ""
        L=0
        R=len(timestamps)-1
        res=""
        while L<=R:
            m=L+(R-L)//2
            if timestamps[m][0]<=timestamp:
                res=timestamps[m][1]
                L=m+1
            else:
                R=m-1

        return res
