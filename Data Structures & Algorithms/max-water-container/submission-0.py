class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0 
        l,r = 0, len(heights)-1

        while l < r:
            curr_volume = (r-l) * min(heights[r], heights[l])
            max_volume = max(max_volume, curr_volume)

            if heights[r] < heights[l]:
                r-=1 
            else:
                l+=1 
            
        return max_volume