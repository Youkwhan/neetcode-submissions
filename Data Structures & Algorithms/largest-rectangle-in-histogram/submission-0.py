class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #store a tuple of (idx, height)
        stack = []
        max_area = 0 
        for idx, height in enumerate(heights):
            
            #while the number is still greater or equal 
                #since we extend 
            prev_start = idx
            while stack and stack[-1][1] >= height:
                prev_start, prev_height = stack.pop()
                prev_area = (idx-prev_start) * prev_height
                max_area = max(max_area, prev_area)
                #add current stack all the way to prev_start
            stack.append((prev_start, height))

        #once the stack is complete
        #I need to complete it for the rest but from the end 
        for index, height in stack:
            max_area = max(max_area , height*(len(heights)-index))
        
        return max_area