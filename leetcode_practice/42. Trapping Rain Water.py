class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []     
        for i, h in enumerate(height):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                currwidth = i - stack[-1] - 1
                currheight = min(height[stack[-1]], height[i]) - height[top]
                res += currwidth * currheight
            stack.append(i)
        return res
     
  
