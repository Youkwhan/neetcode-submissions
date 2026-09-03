class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement], idx]
            seen[n] = idx
        return -1
