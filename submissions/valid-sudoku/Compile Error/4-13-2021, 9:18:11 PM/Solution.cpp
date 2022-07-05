// https://leetcode.com/problems/valid-sudoku

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        set<char> hor[9];
        set<char> ver[9];
        set<char> box[3][3];
        for(int i = 0; i < 9; i++)
            for(int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;
                if (hor[i].count(board[i][j]) == 1) return false;
                if (ver[j].count(board[i][j]) == 1) return false;
                if (box[px][py].count(board[i][j]) == 1) return false;
                hor[i].insert(board[i][j]);
                ver[j].insert(board[i][j]);
                int px = i / 3;
                int py = j / 3;
                box[px][py].insert(board[i][j]);
            }
        return true;
    }
};