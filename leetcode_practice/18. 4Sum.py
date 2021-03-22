class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        def ksum(nums, target, k):
            res = []
            if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target:
                return res
            if k == 2:
                return twosum(nums, target)
            # res = []
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i-1]:
                    for j, num in enumerate(ksum(nums[i+1:], target-nums[i], k-1)):
                        res.append([nums[i]] + num)
            return res
        
        def twosum(nums, target):
            res = []
            l, r = 0, len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum > target or (r < len(nums)-1 and nums[r] == nums[r+1]):
                    r -= 1
                elif sum < target or (l > 0 and nums[l] == nums[l-1]):
                    l += 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res
        
        return ksum(nums, target, 4)
        
