class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [float('inf')]
        for num in arr:
            while stack[-1] <= num:
                node = stack.pop()
                res += node * min(num, stack[-1])
            stack.append(num)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
    
    
