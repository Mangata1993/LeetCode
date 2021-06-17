class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)
        print(stack)
        maxwidth = 0
        for i in range(n-1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                maxwidth = max(maxwidth, i - stack.pop())
        return maxwidth
