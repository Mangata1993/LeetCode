class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left, right = 1, 10 ** 7
        if hour <= len(dist) - 1:
            return -1
        while left < right:
            mid = (left + right) // 2
            total = sum(ceil(num / mid) for num in dist[:-1]) + dist[-1] / mid
            if total > hour:
                left = mid + 1
            else:
                right = mid 
        return left 
    
    
    
        
#          lo, hi, n = 1, 10 ** 7 + 1, len(dist)
#         while lo < hi:
#             speed = lo + (hi - lo) // 2
#             need = dist[-1] / speed + sum((dist[i] + speed - 1) // speed for i in range(n - 1))
#             if need > hour:
#                 lo = speed + 1
#             else:
#                 hi = speed
#         return -1 if lo == 10 ** 7 + 1 else lo  
    
#     is_ontime = lambda s: sum(math.ceil(d / s) for d in dist[:-1]) + dist[-1] / s <= hour
#         low, high = 0, 10**7
#         while low + 1 < high:
#             mid = low + (high - low) // 2
#             if is_ontime(mid):
#                 high = mid
#             else:
#                 low = mid
#         return high if is_ontime(high) else -1
        
        
