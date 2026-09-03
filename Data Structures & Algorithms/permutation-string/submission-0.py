class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        s1_key = [0] * 26
        s2_key = [0] * 26
        for i in range(len(s1)):
            s1_key[ord(s1[i])-ord('a')] +=1
            s2_key[ord(s2[i])-ord('a')] +=1
        
        l_idx = 0
        for idx in range(len(s1),len(s2)):
            if s1_key == s2_key:
                return True
            s2_key[ord(s2[idx])-ord('a')]+=1
            s2_key[ord(s2[l_idx])-ord('a')] -=1
            idx+=1
            l_idx+=1

        return s1_key == s2_key

