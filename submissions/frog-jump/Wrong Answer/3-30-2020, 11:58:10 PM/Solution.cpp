// https://leetcode.com/problems/frog-jump

class Solution {
public:
    bool canCross(vector<int>& stones) {
        typedef pair <int, int> ii;
        int n = stones.size();
        queue <ii> q;
        q.push(ii(0, 0));
        while (!q.empty()) {
            ii u = q.front();
            q.pop();
            int pos = u.first;
            int k = u.second;
            if (binary_search(stones.begin(), stones.end(), pos)) {
                return true;
            }
            if (binary_search(stones.begin(), stones.end(), pos + k - 1)) {
               q.push(ii(pos + k - 1, k - 1)); 
            }
            if (binary_search(stones.begin(), stones.end(), pos + k)) {
               q.push(ii(pos + k, k)); 
            }
            if (binary_search(stones.begin(), stones.end(), pos + k + 1)) {
               q.push(ii(pos + k + 1, k + 1)); 
            }
        }
        return false;
    }
};