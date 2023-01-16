from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board: 
            if not self.validate(row):
                return False
        for i in range(9):
            n_b = [k[i] for k in board ]
            if not self.validate(n_b):
                return False
        for i  in range(0,9,3):
            for k in range(0,9,3):
                n_a = [board[k][i], board[k][i+1], board[k][i+2]]
                n_b = [board[k+1][i], board[k+1][i+1], board[k+1][i+2]]
                n_c = [board[k+2][i], board[k+2][i+1], board[k+2][i+2]]
                n_ = n_a + n_b + n_c
                if not self.validate(n_):
                    return False                  
        return True

    
    def validate(self, arr) -> bool:
        hm = {}
        for i in arr: 
            if i != "." and i in hm.keys():
                return False
            else:
                hm[i] = True
        return True