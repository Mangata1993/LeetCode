class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        p_stack = []
        i_stack = []
        res = ''
        for i in range(len(s)):
            if s[i] == '(':
                p_stack.append(s[i])
                i_stack.append(i)
            elif s[i] == ')':
                if p_stack:
                    p_stack.pop()
                    i_stack.pop()
                else:
                    i_stack.append(i)
        print(i_stack)
        if not i_stack:
            return s
        else:
            for i in range(len(s)):
                if i in i_stack:
                    continue
                else:
                    res += s[i]
        return res
