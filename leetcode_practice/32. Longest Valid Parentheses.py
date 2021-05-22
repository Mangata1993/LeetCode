class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, max_len = [(")", -1)], 0
        for i in range(len(s)):
            if s[i] == ")" and stack[-1][0] == "(":
                stack.pop()
                max_len = max(max_len, i - stack[-1][1])
            else:
                stack.append((s[i], i))
        return max_len
                
#               stk, max_len = [(")", -1)], 0
        
#         for i in range(len(s)):
#             if s[i] == ")" and stk[-1][0] == "(":
#                 stk.pop()
#                 max_len = max(max_len, i-stk[-1][1])
#             else:
#                 stk.append((s[i], i))
#         return max_len
