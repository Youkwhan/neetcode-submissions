class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        #tuple of (temperature, idx)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                output[prev_idx] = idx-prev_idx
            stack.append((temp,idx))
        return output