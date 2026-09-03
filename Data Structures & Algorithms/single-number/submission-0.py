class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr_num = nums[0]
        for i in range(1, len(nums)):
            curr_num = curr_num^nums[i]

        return curr_num
            