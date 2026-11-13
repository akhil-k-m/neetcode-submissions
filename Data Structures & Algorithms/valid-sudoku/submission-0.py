from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        column = defaultdict(set)
        block = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] in ".":
                    continue

                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])
                
                if board[i][j] in column[j]:
                    return False
                else:
                    column[j].add(board[i][j])

                if board[i][j] in block[ i//3, j//3 ]:
                    return False
                else:
                    block[ i//3, j//3 ].add(board[i][j])

        return True       
            
 
