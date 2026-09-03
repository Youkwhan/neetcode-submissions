class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # return number of unique elements
        # array is SORTED in increasing order oh
        """
        1,2,3,4,5,6,1,5,2
                    l     r

        """
        left= 0 # non dup index
        curr = -1
        for right in range(len(nums)):
            if curr != nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                curr = nums[left]
                left += 1
        return left