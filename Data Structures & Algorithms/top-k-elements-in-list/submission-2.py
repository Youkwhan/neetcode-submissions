class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        freqs = [[] for _ in range(len(nums)+1)]

        for num in nums:
            freq_dict[num] = freq_dict.get(num,0)+1
        for num, counts in freq_dict.items():
            freqs[counts].append(num)

        answer = []
        for freq in range(len(freqs)-1,-1,-1):
            for num in freqs[freq]:
                answer.append(num)
                if len(answer) == k:
                    return answer
            