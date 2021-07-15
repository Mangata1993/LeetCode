class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        self.res = 1
        def backtracking(start, split):
            if start >= len(s):
                self.res = max(self.res, split)
            else:
                for i in range(start, len(s)):
                    substr = s[start: i + 1]
                    if substr not in seen:
                        seen.add(substr)
                        backtracking(i + 1, split + 1)
                        seen.remove(substr)
        backtracking(0, 0)
        return self.res
    
    
