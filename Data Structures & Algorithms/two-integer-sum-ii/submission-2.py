class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #two sums in non decreasing order 
        #index 1, index 2 
        #such that they add up to target 
        l,r = 0 , len(numbers)-1
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l+1,r+1]
            elif curr_sum < target:
                l+=1
            else:
                r-=1 
        return None
            