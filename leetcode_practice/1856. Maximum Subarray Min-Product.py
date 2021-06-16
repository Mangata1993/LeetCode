class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left_bound, right_bound = [0] * n, [0] * n
        stack = []
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                left_bound[i] = stack[-1] + 1
            else:
                left_bound[i] = 0
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                right_bound[i] = stack[-1] - 1
            else:
                right_bound[i] = n - 1
            stack.append(i)
            
        # presum = [0] * (n)          为啥这样不行
        # presum[0] = nums[0]
        # for i in range(1, n):
        #     presum[i] = presum[i - 1] + nums[i]
        
        presum = [0] * (n+1)
        presum[0] = nums[0]
        for i in range(n):
            presum[i+1] = presum[i] + nums[i]
        
        maxmin = 0
        for i in range(n):
            maxmin = max(maxmin, nums[i] * (presum[right_bound[i]+1] - presum[left_bound[i]]))
        return maxmin % (10 ** 9 + 7)
    
    
