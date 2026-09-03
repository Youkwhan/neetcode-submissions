class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)

        run_prod = 1 
        for idx in range(len(nums)):
            output[idx] *= run_prod 
            run_prod *= nums[idx]
        
        run_prod = 1
        for idx in range(len(nums)-1, -1,-1):
            output[idx] *= run_prod 
            run_prod *= nums[idx]

        return output
          