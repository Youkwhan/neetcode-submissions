class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_dict = {"(":")", "{":"}", "[":"]"}

        for char in s:
            if char in paren_dict.keys():
                stack.append(paren_dict[char])
            elif char in paren_dict.values():
                if not stack or stack.pop() != char:
                    return False 
        return len(stack) == 0
