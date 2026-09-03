class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            anagram_key = tuple(counts)
            anagram_dict[anagram_key].append(s)
        
        return list(anagram_dict.values())
        