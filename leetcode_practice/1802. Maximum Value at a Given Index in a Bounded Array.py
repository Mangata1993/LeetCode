class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def test(a):
            b = max(a - index, 0)
            res = (b + a) * (a - b + 1) / 2
            b = max(a - ((n - 1) - index), 0)
            res += (b + a) * (a - b + 1) / 2
            return res - a
        
        maxSum -= n
        lower, upper = 0, maxSum
        while lower <= upper:
            mid = (lower + upper) // 2
            if test(mid) > maxSum:
                upper = mid - 1
            else:
                lower = mid + 1
        return lower
    
    
    
