class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash,col_hash,sub_hash = defaultdict(set),defaultdict(set),defaultdict(set)
       
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                if board[r][c] in col_hash[c] or board[r][c] in row_hash[r] or board[r][c] in sub_hash[r//3,c//3]:
                    return False

                col_hash[c].add(board[r][c])  
                row_hash[r].add(board[r][c])
                sub_hash[(r//3,c//3)].add(board[r][c])


        print(row_hash)    
        print(col_hash)    
        print(sub_hash)     
        
        return True


        