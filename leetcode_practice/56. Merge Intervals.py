class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merge = []
        for interval in intervals:
            if merge and interval[0] <= merge[-1][1]:
                merge[-1][1] = max(interval[1], merge[-1][1])
            else:
                merge.append(interval)
        return merge
