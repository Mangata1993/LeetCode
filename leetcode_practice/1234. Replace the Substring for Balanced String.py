class Solution:
    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        i = 0
        res = n = len(s)
        for j, char in enumerate(s):
            count[char] -= 1
            while i < n and all(count[c] <= n/4 for c in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res
    
    
     
