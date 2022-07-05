// https://leetcode.com/problems/n-queens

class Solution:
    def find(self, idx, n, X, column, main_diag, aux_diag):
        if idx == n:
            sol = []
            for i in range(n):
                board = ['.' for _ in range(n)]
                j = X[i]
                board[j] = 'Q'
                sol.append(''.join(board))
            self.solution.append(sol)
            return
        for j in range(n):
            if column[j] and main_diag[idx - j + n - 1] and aux_diag[idx + j]:
                X[idx] = j
                main_diag[idx - j + n - 1] = False
                aux_diag[idx + j] = False
                column[j] = False
                self.find(idx + 1, n, X, column, main_diag, aux_diag)
                X[idx] = -1
                main_diag[idx - j + n - 1] = True
                aux_diag[idx + j] = True
                column[j] = True
                        
                
    def solveNQueens(self, n: int) -> List[List[str]]:
        main_diag = [True] * (2 * n)
        aux_diag = [True] * (2 * n)
        column = [True] * n
        X = [-1] * n
        self.solution = []
        self.find(0, n, X, column, main_diag, aux_diag)
        return self.solution