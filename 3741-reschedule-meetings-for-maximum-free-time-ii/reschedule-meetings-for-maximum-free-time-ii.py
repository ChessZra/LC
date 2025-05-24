class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # prefix sums
        # ez
        intervals = [[startTime[i], endTime[i]] for i in range(len(startTime))]
        intervals.sort()
        N = len(intervals)
        right = [None] * N
        latest_start = eventTime
        for i in range(N - 1, -1, -1):
            start, end = intervals[i]
            right[i] = latest_start - end
            latest_start = start

            if i + 1 < N:
                right[i] = max(right[i], right[i + 1])

        left = [None] * N
        latest_end = 0
        for i in range(N):
            start, end = intervals[i]
            left[i] = start - latest_end
            latest_end = end

            if (i - 1) >= 0:
                left[i] = max(left[i], left[i - 1])

        res = 0
        for i in range(N):
            # Reschedule to the same section (maximize)
            l = 0 if i == 0 else intervals[i - 1][1]
            r = eventTime if i == N - 1 else intervals[i + 1][0]
            res = max(res, intervals[i][0] - l + r - intervals[i][1])

            # Reschedule to the left
            if i > 0:
                size = intervals[i][1] - intervals[i][0]
                if size <= left[i - 1]:
                    res = max(res, (eventTime if i == N - 1 else intervals[i + 1][0]) - intervals[i - 1][1])

            # Reschedule to the right
            if i < N - 1:
                size = intervals[i][1] - intervals[i][0]
                if size <= right[i + 1]:
                    res = max(res, intervals[i + 1][0] - (0 if i == 0 else intervals[i - 1][1]))

        return res