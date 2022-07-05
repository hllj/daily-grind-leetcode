// https://leetcode.com/problems/magnetic-force-between-two-balls

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position = sorted(position)
        l = 1
        r = position[-1] - position[0]
        res = -1
        while l <= r:
            mid = (l + r) // 2
            print('check', mid)
            cnt = 1
            curr = position[0]
            for i in range(1, n):
                if position[i] - curr >= mid:
                    cnt += 1
                    curr = position[i]
            print('cnt', cnt)
            if cnt >= m:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res