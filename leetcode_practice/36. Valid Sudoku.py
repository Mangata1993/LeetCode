class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                cur = board[i][j]
                if cur != '.':                  #别忘了加这个条件！！
                    if (i, cur) in seen or (cur, j) in seen or (i//3, j//3, cur) in seen:
                        return False
                    seen.add((i, cur))
                    seen.add((cur, j))
                    seen.add((i//3, j//3, cur))
        return True
    
   
