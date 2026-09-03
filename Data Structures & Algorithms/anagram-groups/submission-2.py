class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group the key and use that 
        anagram_dict = {}

        for s in strs:
            key = [0 for _ in range(26)]

            for c in s:
                key[ord(c)-ord('a')]+=1 
            
            key = tuple(key)
            if key in anagram_dict:
                anagram_dict[key].append(s)
            else:
                anagram_dict[key] = [s]
        
        return [values for values in anagram_dict.values()]
