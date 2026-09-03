class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = defaultdict(set)
        col_sets = defaultdict(set)
        box_sets = defaultdict(set)

        for row in range(9):
            for col in range(9):
                curr_val = board[row][col]
                if curr_val == ".":
                    continue 
                
                if curr_val in row_sets[row] or curr_val in col_sets[col] or curr_val in box_sets[(row//3,col//3)]:
                    return False
                row_sets[row].add(curr_val)
                col_sets[col].add(curr_val)
                box_sets[(row//3,col//3)].add(curr_val)

        return True 
