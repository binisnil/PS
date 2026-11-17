class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        i, n = 0, len(intervals)
        s, e = newInterval

    # 1. 앞쪽 (안 겹침)
        while i < n and intervals[i][1] < s:
            res.append(intervals[i]); i += 1

    # 2. 겹치는 구간 병합
        while i < n and intervals[i][0] <= e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            i += 1
        res.append([s, e])

    # 3. 뒤쪽 (안 겹침)
        while i < n:
            res.append(intervals[i]); i += 1
        return res