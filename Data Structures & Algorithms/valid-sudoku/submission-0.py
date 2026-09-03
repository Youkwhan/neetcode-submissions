from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_sets = defaultdict(set)
        col_sets = defaultdict(set)
        square_sets = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                curr_num = board[row][col]
                if curr_num.isnumeric():
                    row_set = row_sets[row]
                    col_set = col_sets[col]
                    square_set = square_sets[(row//3,col//3)]

                    if curr_num in row_set or curr_num in col_set or curr_num in square_set:
                        return False 
                    row_set.add(curr_num)
                    col_set.add(curr_num)
                    square_set.add(curr_num)
        return True 


        