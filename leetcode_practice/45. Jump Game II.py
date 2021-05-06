class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        farthest = 0
        count = 0
        current_end = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if current_end == i:
                current_end = farthest
                count += 1
        return count
               
