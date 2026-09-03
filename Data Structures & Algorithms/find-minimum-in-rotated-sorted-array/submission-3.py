class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
            find the minimum, binary search
                     lr 
            [3,4,5,6,1,2]
             0 1 2 3 4 5

            1. we need to find the mid poitn of pivot
            2. we need to find which partiiton is lower
            2. binary search until we find lowest? TFFFF?
        """
        left, right = 0, len(nums)-1

        while left < right:
            # FFFFPTTT
            # left most, lower mid
            # left = mid + 1
            # right = mid
            mid = left + (right-left) // 2
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
