class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x[1])
        prev_end = intervals[0][1]
        unique = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev_end:
                unique += 1
                prev_end = intervals[i][1]
            
        return len(intervals) - unique       
                
