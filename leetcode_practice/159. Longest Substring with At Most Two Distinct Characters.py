class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3:
            return len(s)
        l, r = 0, 0
        max_len = 2
        mp = {}
        while r < len(s):
            mp[s[r]] = r
            r += 1
            if len(mp) == 3:
                del_idx = min(mp.values())
                del mp[s[del_idx]]
                l = del_idx + 1
            max_len = max(max_len, r - l)
        return max_len
                    
