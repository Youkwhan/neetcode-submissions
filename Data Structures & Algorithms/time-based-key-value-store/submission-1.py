class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # 1,2,3,4,5
        # T T T T F
        # 
        if key not in self.timemap:
            return ""

        res = ""
        value_list = self.timemap[key]

        l,r = 0, len(value_list)-1

        while l <= r:
            m = (l+r)//2
            if value_list[m][0] <= timestamp:
                res = value_list[m][1] # we want to update the value as long as it is valid, when target or lower
                l = m+1
            else:
                r = m -1
        return res
