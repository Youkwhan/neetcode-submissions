from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #shortest substring of s
        if len(s) < len(t):
            return "" 
        counter_t = Counter(t)
        counter_s = {}
        need = len(counter_t)
        have = 0 

        shortest_len = float("inf")
        shortest_pair = []

        l = 0
        for r in range(len(s)):
            counter_s[s[r]] = counter_s.get(s[r],0) + 1
            if s[r] in counter_t and counter_t[s[r]] == counter_s[s[r]]:
                have +=1 
            
            while have == need:
                curr_len = (r-l)
                if curr_len < shortest_len:
                    shortest_pair = [l,r]
                    shortest_len = curr_len
                counter_s[s[l]]-=1 
                #that means we suddenly dont have enough
                if counter_s[s[l]]+1 == counter_t[s[l]]:
                    have -=1 
                l+=1 
                
        return s[shortest_pair[0]:shortest_pair[1]+1] if shortest_len != float("inf") else ""
