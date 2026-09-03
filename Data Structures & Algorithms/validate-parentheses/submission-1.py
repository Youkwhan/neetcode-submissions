class Solution:
    def isValid(self, s: str) -> bool:
        #check for valid parens
        #every bracket is closed 
        #when we see open we store it 
        #when we see close we pop and check
        parens = {')':'(','}':'{',']':'['}
        stack = []

        for c in s:
            if c in parens:
                if not stack or stack.pop() != parens[c]:
                    return False 
            else:
                stack.append(c)
        return not stack

            
