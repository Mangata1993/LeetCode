class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = 1
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]
        for i in reversed(range(n)):
            res[i] = r * res[i]
            r = r * nums[i]
            
        return res
