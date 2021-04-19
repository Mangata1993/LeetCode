class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 1
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt <= 2:
                nums[j] = nums[i]
                j += 1
        return j
