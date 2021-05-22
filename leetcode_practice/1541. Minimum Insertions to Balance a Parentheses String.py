class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        miss_left_count = 0
        miss_right_count = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append('(')
            else:       # s[i] == ')'
                if len(stack) > 0:
                    if i < len(s) - 1 and s[i+1] == ')':
                        stack.pop()
                        i += 1
                    else:
                        miss_right_count += 1
                        stack.pop()
                else:
                    if i < len(s) - 1 and s[i+1] == ')':
                        miss_left_count += 1
                        i += 1
                    else:
                        miss_left_count += 1
                        miss_right_count += 1
            i += 1
        print(miss_left_count, miss_right_count, stack)
        if stack:
            miss_right_count += len(stack) * 2
        
        return miss_left_count + miss_right_count
                
