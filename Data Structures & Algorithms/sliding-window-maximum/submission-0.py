from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #(idx)
        queue = deque([])
        answer = []

        for i in range(k):
            curr_num = nums[i]
            while queue and nums[queue[-1]] < curr_num:
                queue.pop()
            queue.append(i)
        
        answer.append(nums[queue[0]])

        for i in range(k,len(nums)):
            curr_num = nums[i]
            #is the current head out of range?
            if queue[0] == i-k:
                queue.popleft()

            while queue and nums[queue[-1]] < curr_num:
                queue.pop()
            queue.append(i)
            answer.append(nums[queue[0]])
        return answer 