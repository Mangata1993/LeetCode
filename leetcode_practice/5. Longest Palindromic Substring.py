class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def helper(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        for i in range(len(s)):
            res = max(helper(i, i, s), helper(i, i+1, s), res, key = len)
        return res
