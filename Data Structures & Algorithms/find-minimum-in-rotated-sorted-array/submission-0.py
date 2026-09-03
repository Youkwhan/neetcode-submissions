class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1 

        while l <= r:
            midpoint = (l+r)//2 
            if nums[midpoint] < nums[r]:
                r = midpoint 
            else:
                l = midpoint+1

            

        return nums[midpoint]