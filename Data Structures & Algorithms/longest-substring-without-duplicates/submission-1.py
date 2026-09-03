class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_dict = {}
        answer = 0 
        start_idx = 0 
        for idx, s in enumerate(s):
            if s in letter_dict:
                start_idx = max(start_idx, letter_dict[s]+1)
            letter_dict[s] = idx 
            answer = max(answer, idx-start_idx+1)
        return answer
            

        