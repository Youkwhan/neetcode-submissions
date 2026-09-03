class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break 
            #keep going if the first number keeps repeating
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            j = i+1
            k = len(nums)-1 

            while j < k:
                curr_sum = nums[i]+nums[j]+nums[k]

                if curr_sum > 0:
                    k-=1
                elif curr_sum < 0:
                    j+=1
                else:
                    output.append([nums[i],nums[j],nums[k]])
                    #now we have to avoid duplicates
                    #so one value must change at least 
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1 
        return output
