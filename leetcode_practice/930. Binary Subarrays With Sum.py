class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = collections.defaultdict(int)
        count[0] = 1
        presum = 0
        res = 0
        for num in nums:
            presum += num
            res += count[presum - goal]
            count[presum] += 1
        return res
