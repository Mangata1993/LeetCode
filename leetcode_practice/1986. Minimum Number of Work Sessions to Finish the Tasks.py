class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort()
        n = len(tasks)
        
        def canFinish(num):
            if num * sessionTime < sum(tasks):
                return False
            buckets = [0] * num
        
            def backtracking(idx, buckets):
                if idx == n:
                    return True
                for j in range(num):
                    buckets[j] += tasks[idx]
                    if buckets[j] <= sessionTime:
                        if backtracking(idx + 1, buckets):
                            return True
                    buckets[j] -= tasks[idx]
                return False
            
            return backtracking(0, buckets)
        
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        return left 
            
