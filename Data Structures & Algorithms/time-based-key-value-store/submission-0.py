class TimeMap:

    def __init__(self):
        self.timemap = {}
        #list of timestamp value
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        
        answer = ""
        value_list = self.timemap[key]

        l,r = 0, len(value_list)-1
        while l <= r:
            midpoint = (l+r)//2
            if value_list[midpoint][0] <= timestamp:
                answer = value_list[midpoint][1]
                l = midpoint+1
            else:
                r = midpoint-1
        return answer






        
