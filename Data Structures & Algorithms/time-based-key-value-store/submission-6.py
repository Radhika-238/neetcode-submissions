class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap or timestamp < self.timeMap[key][0][0]:
            return ''

        low = 0
        high = len(self.timeMap[key]) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.timeMap[key][mid][0] == timestamp:
                return self.timeMap[key][mid][1]
            elif self.timeMap[key][mid][0] > timestamp:
                high = mid - 1
            else:
                low = mid + 1

        return self.timeMap[key][high][1]
               


