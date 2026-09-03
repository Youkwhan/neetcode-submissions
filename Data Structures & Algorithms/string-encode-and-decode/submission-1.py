class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "%" + s
        return output
            
    def decode(self, s: str) -> List[str]:
        answer = []
        idx = 0 
        while idx < len(s):
            end = idx 
            while s[end] != "%":
                end+=1 
            number = int(s[idx:end])
            idx = end+1
            letter = s[idx:idx+number]
            answer.append(letter)
            idx = idx+number
        return answer 






#we need a stop charecter that we can use to denote that it is a space 