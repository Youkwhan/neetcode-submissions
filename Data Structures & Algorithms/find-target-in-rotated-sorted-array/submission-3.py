class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        rotated sorted array (unique)
        integer target
        return index or -1 if not present       
        
        1. find the pivot 
        FFFTTT 
        - lower mid, right = mid (since it is the potential answer)
        2. find the side
        3. binary searhc target
        """
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        left = 0
        right = len(nums)-1

        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1
        
        while left <= right:
            mid = left + (right-left)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1