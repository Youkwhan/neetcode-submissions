class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l,r = 0, ROWS*COLS-1 

        while l<=r:
            midpoint = (l+r)//2

            row = midpoint//COLS
            col = midpoint%COLS
            guess = matrix[row][col]
            if guess < target:
                l = midpoint +1 
            elif guess > target:
                r = midpoint -1 
            else:
                return True
        return False 

