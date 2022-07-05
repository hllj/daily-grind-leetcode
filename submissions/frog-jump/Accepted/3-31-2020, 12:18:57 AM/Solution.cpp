// https://leetcode.com/problems/frog-jump

class Solution {
public:
    bool canCross(vector<int>& stones) {
        typedef pair <int, int> ii;
        int n = stones.size();
        queue <ii> q;
        q.push(ii(stones[0], 0));
        set <ii> visited;
        visited.insert(ii(stones[0], 0));
        while (!q.empty()) {
            ii u = q.front();
            q.pop();
            int pos = u.first;
            int k = u.second;
            if (pos == stones[n - 1]) {
                return true;
            }
            if (binary_search(stones.begin(), stones.end(), pos + k - 1) && visited.count(ii(pos + k - 1, k -1)) == 0) {
               q.push(ii(pos + k - 1, k - 1));
                visited.insert(ii(pos + k - 1, k - 1));
            }
            if (binary_search(stones.begin(), stones.end(), pos + k) && visited.count(ii(pos + k, k)) == 0) {
               q.push(ii(pos + k, k)); 
                visited.insert(ii(pos + k, k));
            }
            if (binary_search(stones.begin(), stones.end(), pos + k + 1) && visited.count(ii(pos + k + 1, k + 1)) == 0) {
               q.push(ii(pos + k + 1, k + 1)); 
                visited.insert(ii(pos + k + 1, k + 1));
            }
        }
        return false;
    }
};