class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        delimiter = "#"
        for word in strs:
            count = len(word)
            encode = f'{count}{delimiter}{word}'
            res.append(encode)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        delimiter = "#"
        left = 0
        while left < len(s):
            right = left
            while s[right] != delimiter:
                right += 1
            count = int(s[left:right])
            res.append(s[right+1:right+count+1])
            
            left = right + count+1
        return res