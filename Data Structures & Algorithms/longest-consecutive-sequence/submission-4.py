class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_sets = set(nums)
        answer = 0
        for num in num_sets:
            if num-1 in num_sets:
                continue 
            curr_seq_len = 0
            while num in num_sets:
                curr_seq_len+=1
                num+=1 
            
            answer = max(curr_seq_len, answer)
            
        return answer