class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = {}
        
        self.timeMap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ''

        timestamps = list(self.timeMap[key].keys())
        timestamps.sort()
        low = 0
        high = len(timestamps) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2
            if timestamps[mid] == timestamp:
                result = mid
                break
            elif timestamps[mid] > timestamp:
                high = mid - 1
            else:
                result = mid
                low = mid + 1
        if result == -1:
            return ''

        return self.timeMap[key][timestamps[result]]
               


