class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        answer = r

        while l <= r:
            guess = (l+r)//2 
            time_taken = 0
            for pile in piles:
                time_taken+=math.ceil(pile/guess)
            if time_taken <= h:
                answer = guess 
                r = guess-1
            else:
                l = guess+1
        return answer 


