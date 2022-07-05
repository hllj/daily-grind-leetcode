// https://leetcode.com/problems/word-search-ii

class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    def dfs(self, avail, board, idx, word, x, y, n, m):
        if idx == len(word) - 1:
            return True
        check = False
        for i in range(4):
            new_x = x + self.dx[i]
            new_y = y + self.dy[i]
            if new_x < 0 or new_x == n or new_y < 0 or new_y == m:
                continue
            if (board[new_x][new_y] == word[idx + 1]) and (avail[new_x][new_y]):
                avail[new_x][new_y] = False
                res = self.dfs(avail, board, idx + 1, word, new_x, new_y, n, m)
                check = check or res
                if check == True:
                    return True
                avail[new_x][new_y] = True
        return check
                
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        avail = [[True for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    avail[i][j] = False
                    check = self.dfs(avail, board, 0, word, i, j, n, m)
                    if check == True:
                        return True
                    avail[i][j] = True
        return False
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        # avail = [[True for _ in range(m)] for _ in range(n)]
        res = []
        for word in words:
            avail = [[True for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if board[i][j] == word[0]:
                        avail[i][j] = False
                        check = self.dfs(avail, board, 0, word, i, j, n, m)
                        if check == True:
                            res.append(word)
                        avail[i][j] = True
        return res