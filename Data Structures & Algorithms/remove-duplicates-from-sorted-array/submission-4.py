class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # return number of unique elements
        # array is SORTED in increasing order oh
        """
        1,2,3,4,5,6,1,5,2
                    l     r

        2,1,2,3,3,4,4,4
        l   r
        if it's different replace, and then continue until we find next different
        OH that way we dont need to check curr bcz we arent swapping
        [2,10,10,30,30,30]
               lr
        """
        if len(nums) == 0:
            return 0

        left = 1
        for right in range(1, len(nums)):
          if nums[right] != nums[right-1]:
            nums[left] = nums[right]
            left += 1
        return left