class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx in range(len(nums)):
            complement = target - nums[idx]
            if complement in seen:
                return [seen[complement], idx]
            else:
                seen[nums[idx]] = idx
        return -1
