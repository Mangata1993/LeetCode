class Solution:
    def checkValidString(self, s: str) -> bool:
        lower = upper = 0
        for i in range(len(s)):
            if s[i] == '(':
                lower += 1
            else:
                lower -= 1
            if s[i] != ')':
                upper += 1
            else:
                upper -= 1
            if upper < 0:
                return False
            lower = max(lower, 0)
        return lower == 0
