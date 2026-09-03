class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        most_f = 0
        l_idx = 0 
        answer = 0
        for idx in range(len(s)):
            char_count[s[idx]] = char_count.get(s[idx],0)+1

            if char_count[s[idx]] > most_f:
                most_f = char_count[s[idx]]


            if idx-l_idx+1 - most_f > k:
                char_count[s[l_idx]] -= 1
                #check most frequent now 
                l_idx+=1 
            answer = max(answer, idx-l_idx+1)
        return answer
            



        