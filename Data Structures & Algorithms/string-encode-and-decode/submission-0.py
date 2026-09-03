class Solution:

    def encode(self, strs: List[str]) -> str:
        output = [] 
        for s in strs:
            output.append(str(len(s))+"#"+s)
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            
            #number is (i to j-1) but python end non included
            number_str = int(s[i:j])
            letter_start = j+1
            letter_end = letter_start + number_str
            letter_str = s[letter_start:letter_end]
            output.append(letter_str)
            i = letter_end
        return output

