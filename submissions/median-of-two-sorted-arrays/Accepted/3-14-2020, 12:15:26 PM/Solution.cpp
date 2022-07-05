// https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int x = nums1.size();
  int y = nums2.size();

  if (x > y) {
    nums1.swap(nums2);
    int tmp = x;
    x = y;
    y = tmp;
  }
const int INF = (int) 1e9;
  int left = 0;
  int right = x;
  int partitionX, partitionY;
  while (left <= right) {
    partitionX = (left + right) / 2;
    partitionY = (x + y + 1) / 2 - partitionX;
    int maxLeftX = partitionX - 1 < 0 ? -INF : nums1[partitionX - 1];
    int minRightX = partitionX == x ? INF : nums1[partitionX];
    int maxLeftY = partitionY - 1 < 0 ? -INF : nums2[partitionY - 1];
    int minRightY = partitionY == y ? INF : nums2[partitionY];
  
    cout << left << " " << right << "\n";
    //cout << partitionX << " " << partitionY << "\n";
    //cout << "Max Left X" << maxLeftX << "\n";
    //cout << "Max Left Y" << maxLeftY << "\n";
    //cout << "Min Right X" << minRightX << "\n";
    //cout << "Min Right Y" << minRightY << "\n";
    //cout << "------" << "\n";

    if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
      if ((x + y) % 2) return max(maxLeftX, maxLeftY);
      else return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0;
    }

    if (maxLeftX > minRightY) right = partitionX - 1;
    else 
      left = partitionX + 1;
  }
  return 0;
    }
};