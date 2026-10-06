class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        prev = intervals[0]
        remove = 0

        for start, end in intervals[1:]:
            if prev[1] > start:
                if prev[1] >= end:
                    prev = [start, end]
                remove += 1
            else:
                prev = [start, end]

        return remove
            