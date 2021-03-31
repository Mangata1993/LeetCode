class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if sum(ceil(p / mid) for p in piles) > h:
                left = mid + 1
            else:
                right = mid
        return left
    
   # 或者 left, right = 1, max(piles)                        #注意这个和上面的区别。两个都能跑通
   #      while left <= right:
   #          mid = (left + right) // 2
   #          if sum(ceil(p / mid) for p in piles) > h:
   #              left = mid + 1
   #          else:
   #              right = mid - 1
   #      return left
    
    
    
        #    l, r = 1, max(piles)
        # while l < r:
        #     m = (l + r) / 2
        #     if sum((p + m - 1) / m for p in piles) > H:
        #         l = m + 1
        #     else:
        #         r = m
        # return l
