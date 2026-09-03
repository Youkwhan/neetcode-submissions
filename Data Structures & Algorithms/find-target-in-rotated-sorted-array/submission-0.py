class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            midpoint = (l+r)//2

            if nums[midpoint] == target:
                return midpoint

            #guess is after the pivot
            if nums[midpoint] <= nums[r]:
                if target < nums[midpoint] or target > nums[r]:
                    r = midpoint-1
                else:
                    l = midpoint+1
            #guess is before the pivot
            else:
                if target > nums[midpoint] or target < nums[l]:
                    l = midpoint+1
                else:
                    r = midpoint-1
        return -1
        
