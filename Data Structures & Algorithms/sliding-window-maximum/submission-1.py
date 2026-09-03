class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        In each window return the list of the max

        """
        if not k or not nums:
            return []
        res = []
        curMax = float("-inf")
        window = defaultdict(int)

        for i in range(k):
            window[nums[i]] += 1
            curMax = max(curMax, nums[i])
        
        res.append(curMax)
        
        left = 0
        for right in range(k, len(nums)):
            # add the new right
            window[nums[right]] += 1
            #shrink left if exceed
            while (right - left +1) > k:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
            # compare new max
            curMax = max(window.keys())
            # add to list
            res.append(curMax)
        return res