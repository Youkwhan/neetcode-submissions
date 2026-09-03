class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_sets = set(nums)
        longest_seq = 0
        for num in nums:
            if num-1 not in num_sets:
                length = 1 
                while num+length in num_sets:
                    length+=1
                longest_seq = max(longest_seq, length)
        return longest_seq
