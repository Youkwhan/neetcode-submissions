class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            return result where it is number of days after ith before a warmer temp
            if none return 0

            [30,38,30,36,35,40,28]
            [1,4,1,2,1,0,0]
            [(40,5), (28,6)]
        """
        res = [0] * len(temperatures)

        stack = [] # (temperature, idx)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append((temp, i))
        return res