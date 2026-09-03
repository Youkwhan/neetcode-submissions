class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def helper(path, n, open_count, closed_count):
            if closed_count == n:
                output.append("".join(path))
                return 
            
            #we can always open 
            if open_count < n:
                path.append("(")
                helper(path, n, open_count+1, closed_count)
                path.pop()
            
            if closed_count < open_count:
                path.append(")")
                helper(path, n, open_count, closed_count+1)
                path.pop()
        helper([],n,0,0)
        return output 
