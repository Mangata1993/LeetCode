class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def count(target):
            sumsw, cnt = 0, 0
            for s in sweetness:
                sumsw += s
                if sumsw >= target:
                    cnt += 1
                    sumsw = 0
            return cnt
        
        left, right = min(sweetness), sum(sweetness)//(K+1)
        while left <= right:
            mid = (left + right) // 2
            if count(mid) < K+1:
                right = mid - 1
            else:
                left = mid + 1
        return right
        
