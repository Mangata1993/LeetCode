class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtracking(first, tmp):
            if len(tmp) == k:
                res.append(tmp[:])
            for i in range(first, n + 1):
                tmp.append(i)
                backtracking(i + 1, tmp)
                tmp.pop()
            
        backtracking(1, [])
        return res
