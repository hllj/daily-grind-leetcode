// https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l = 0
        r = n - 1
        idx = 0
        while l <= r:
            m = (l + r) // 2
            if arr[m] < x:
                l = m + 1
            elif arr[m] > x:
                r = m - 1
            elif arr[m] == x:
                idx = m
                break
            dis_m = abs(arr[m] - x)
            dis_i = abs(arr[idx] - x)
            if (dis_m < dis_i) or (dis_m == dis_i and arr[m] < arr[idx]):
                idx = m
        cnt = 1
        print('idx', idx)
        l = idx
        r = idx
        while cnt < k:
            can_l = l - 1
            can_r = r + 1
            if (can_l < 0):
                cnt += 1
                r = can_r
            elif (can_r == n):
                cnt += 1
                l = can_l
            elif (can_l >= 0 and can_r < n):
                dis_l = abs(arr[can_l] - x)
                dis_r = abs(arr[can_r] - x)
                if (dis_l < dis_r) or (dis_l == dis_r and arr[can_l] < arr[can_r]):
                    l = can_l
                else:
                    r = can_r
                cnt += 1
        print(l, r)
        return arr[l: r + 1]