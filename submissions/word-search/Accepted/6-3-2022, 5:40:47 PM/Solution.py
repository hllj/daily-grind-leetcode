// https://leetcode.com/problems/word-search

class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    def dfs(self, board, idx, word, x, y):
        if idx == len(word) - 1:
            return True
        check = False
        for i in range(4):
            new_x = x + self.dx[i]
            new_y = y + self.dy[i]
            if new_x < 0 or new_x == self.n or new_y < 0 or new_y == self.m:
                continue
            if (board[new_x][new_y] == word[idx + 1]) and (self.avail[new_x][new_y]):
                self.avail[new_x][new_y] = False
                res = self.dfs(board, idx + 1, word, new_x, new_y)
                check = check or res
                self.avail[new_x][new_y] = True
        return check
                
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.n = len(board)
        self.m = len(board[0])
        self.avail = [[True for _ in range(self.m)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == word[0]:
                    self.avail[i][j] = False
                    check = self.dfs(board, 0, word, i, j)
                    if check == True:
                        return True
                    self.avail[i][j] = True
        return False