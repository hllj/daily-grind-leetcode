// https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    can = []
    def search(self, a, b, flag):
        n = len(a)
        m = len(b)
        l1 = 0
        r1 = n - 1
        while l1 <= r1:
            m1 = (l1 + r1) // 2
            no_lower = m1
            no_upper = n - 1 - m1
            l2 = 0
            r2 = m - 1
            i2 = -1
            while (l2 <= r2):
                m2 = (l2 + r2) // 2
                if b[m2] >= a[m1]:
                    i2 = m2
                    r2 = m2 - 1
                else:
                    l2 = m2 + 1
            if i2 == -1:
                no_lower += m
            else:
                no_lower += i2
                no_upper += m - i2
            if ((n + m) % 2 == 1) and (no_lower == no_upper):
                print('candidate even ', flag, m1)
                self.can.append(a[m1])
            if ((n + m) % 2 == 0) and abs(no_lower - no_upper) <= 1:
                print('candidate odd ', flag, m1)
                self.can.append(a[m1])
            if no_lower < no_upper:
                l1 = m1 + 1
            else:
                r1 = m1 - 1
            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.can = []
        self.search(nums1, nums2, 'a')
        print('------------')
        self.search(nums2, nums1, 'b')
        if len(self.can) == 1:
            return self.can[0]
        else:
            return (self.can[0] + self.can[1]) / 2.0
        
        