class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}
        freq_list = [[] for _ in range( len(nums)+1)]
        for num in nums:
            freq_dict[num] = freq_dict.get(num,0)+1 
        
        for num, freq in freq_dict.items():
            freq_list[freq].append(num)
        
        output = [] 
        
        for i in range(len(freq_list)-1,0,-1):
            for num in freq_list[i]:
                output.append(num)
                if len(output) == k:
                    return output 
        return None 
