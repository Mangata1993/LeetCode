class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for idx, n in enumerate(intervals):
            if newInterval[0] > n[1]:
                res.append(n)
            elif newInterval[1] < n[0]:
                res.append(newInterval)
                return res + intervals[idx:]
            else:
                newInterval[0] = min(newInterval[0], n[0])
                newInterval[1] = max(newInterval[1], n[1])
        res.append(newInterval)
        return res
                
                
#     res, n = [], newInterval
#     for index, i in enumerate(intervals):
#         if i.end < n.start:
#             res.append(i)
#         elif n.end < i.start:
#             res.append(n)
#             return res+intervals[index:]  # can return earlier
#         else:  # overlap case
#             n.start = min(n.start, i.start)
#             n.end = max(n.end, i.end)
#     res.append(n)
#     return res
