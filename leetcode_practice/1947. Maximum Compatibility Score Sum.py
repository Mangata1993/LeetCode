class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        self.res = 0
        sm = [0] * m
        def calc(a, b):
            ans = 0
            for i in range(len(a)):
                if a[i] == b[i]:
                    ans += 1
            return ans
        
        def dfs(idx, curr):
            if idx == m:
                self.res = max(self.res, curr)
            for i in range(m):
                if not sm[i]:
                    sm[i] = True
                    score = calc(students[idx], mentors[i])
                    
                    dfs(idx + 1, curr + score)
                    sm[i] = False
            return self.res
        
        return dfs(0, 0)
        
        
