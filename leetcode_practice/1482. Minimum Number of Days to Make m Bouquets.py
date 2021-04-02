class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        def canmake(daynum, m, k):
            tmpk = k
            for day in bloomDay:
                if day <= daynum:
                    tmpk -= 1
                    if tmpk == 0:
                        m -= 1
                        tmpk = k
                else:
                    tmpk = k
            return m <= 0                               # must be m <= 0, instead of m==0
        
        left, right = -1, 10 ** 9
        while left < right:
            mid = (left + right) // 2
            if canmake(mid, m, k):
                right = mid
            else:
                left = mid + 1
        return left
      
      
      
