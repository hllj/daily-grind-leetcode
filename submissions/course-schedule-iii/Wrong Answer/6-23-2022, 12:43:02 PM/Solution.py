// https://leetcode.com/problems/course-schedule-iii

import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # courses = sorted(courses, key=lambda x: x[1])
        # print(courses)
        time = 0
        heap = []
        for course in courses:
            if course[0] + time <= course[1]:
                time += course[0]
                heapq.heappush(heap, -course[0])
            else:
                if len(heap) > 0:
                    max_duration_course = heap[0]
                    time += max_duration_course
                    heapq.heappushpop(heap, (-course[0]))
                    time += course[0]
        return len(heap)
                