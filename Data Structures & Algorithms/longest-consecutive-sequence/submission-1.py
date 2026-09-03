class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_sets = set(nums)
        longest_seq = 0
        for num in nums:
            if num-1 not in num_sets:
                curr_seq_len = 1
                curr = num+1 
                while curr in num_sets:
                    curr_seq_len+=1
                    curr+=1 
                longest_seq = max(longest_seq, curr_seq_len)
        return longest_seq
