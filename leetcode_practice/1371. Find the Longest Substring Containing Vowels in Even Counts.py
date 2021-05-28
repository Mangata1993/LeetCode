class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/solution/1371-mei-ge-yuan-yin-bao-han-ou-shu-ci-d-nmqp/
        vowels = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        seen = {0:-1}       #为什么初始化为0：-1？
        state = 0           #state是为了检测两次state中间是否出现了偶数次的元音
        res = 0
        for i, char in enumerate(s):
            if char in vowels:
                state ^= vowels[char]
            if state in seen:
                res = max(res, i - seen[state])
            else:
                seen[state] = i
        return res
