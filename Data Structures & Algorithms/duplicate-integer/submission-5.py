class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for element in nums:
            dup[element] = dup.get(element, 0) + 1
            if dup[element] > 1:
                return True
        return False