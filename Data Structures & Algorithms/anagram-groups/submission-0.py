class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {} 

        for s in strs:
            key = self.create_key(s)
            if key in anagram_dict:
                anagram_dict[key].append(s)
            else:
                anagram_dict[key] = [s]
        return list(anagram_dict.values())

    
    def create_key(self,s):
        letter_keys = [0] * 26
        for c in s:
            letter_keys[ord(c)-ord('a')] +=1 
        return tuple(letter_keys)
