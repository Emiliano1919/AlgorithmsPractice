import bisect

class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ''
        timestamps = self.m[key]
        # Search for timestamp using bisect_right on the tuple (timestamp, chr(127))
        idx = bisect.bisect_right(timestamps, (timestamp, chr(127))) - 1
        if idx >= 0:
            return timestamps[idx][1]
        return ''
