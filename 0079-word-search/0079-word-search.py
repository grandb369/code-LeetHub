class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,w):
            if not w:
                return True
            if 0<=r<len(board)and 0<=c<len(board[0]) and board[r][c]==w[0]:
                temp=board[r][c]
                board[r][c]='#'
                w=w[1:]
                val=dfs(r-1,c,w)or dfs(r+1,c,w)or dfs(r,c+1,w)or dfs(r,c-1,w)
                board[r][c]=temp
                return val
            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,word):
                    return True
        return False