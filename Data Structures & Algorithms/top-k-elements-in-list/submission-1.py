from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #so we want to make sure to do this in linear time 

        #key is number, value is frequency
        counter_dict = defaultdict(int)
        for num in nums:
            counter_dict[num]+=1 

        #counter_list
        #we want an extra so it is 1 indexed
        counter_list = [[] for _ in range(len(nums)+1)]
        for key, value in counter_dict.items():
            counter_list[value].append(key)


        output = []
        for idx in range(len(counter_list)-1,-1,-1): 
            for num in counter_list[idx]:
                output.append(num)
                if len(output) == k:
                    return output

