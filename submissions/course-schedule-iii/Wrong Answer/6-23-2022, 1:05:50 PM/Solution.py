// https://leetcode.com/problems/course-schedule-iii

import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda x: x[1])
        n = len(courses)
        m = courses[-1][1]
        f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for j in range(m):
            f[0][j] = 0
        res = 0
        for j in range(m):
            for i in range(1, n + 1):
                f[i][j] = f[i - 1][j]
                if j >= courses[i - 1][0] and j <= courses[i - 1][1]:
                    f[i][j] = max(f[i][j], f[i - 1][j - courses[i - 1][0]] + 1)
                res = max(res, f[i][j])
        return res