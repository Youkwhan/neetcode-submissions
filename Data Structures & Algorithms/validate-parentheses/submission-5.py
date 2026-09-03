class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}':'{', ']':'[',')':'('}
        stack = []
        
        for c in s:
            if c in mapping:
                if not stack or mapping[c] != stack.pop():
                    return False
            else:
                stack.append(c)

        return True if not stack else False