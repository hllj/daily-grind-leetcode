// https://leetcode.com/problems/queue-reconstruction-by-height


class Solution:
    def reconstructQueue(self, people):
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue