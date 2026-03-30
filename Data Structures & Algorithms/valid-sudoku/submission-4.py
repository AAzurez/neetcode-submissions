class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        Array = [set() for _ in range(9)]

        for i in range(len(board)):
            hori = set()
            vert = set()
            for j in range(len(board)):
                
                idx = (i // 3) * 3 + (j // 3)
                
                if board[i][j] != ".":
                    if board[i][j] not in Array[idx]:
                        Array[idx].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in hori:
                        hori.add(board[i][j])
                    else:
                        return False

                if board[j][i] != ".":
                    if board[j][i] not in vert:
                        vert.add(board[j][i])
                    else:
                        return False
                else:
                    continue
                 
        return True