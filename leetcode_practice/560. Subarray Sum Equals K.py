class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = collections.defaultdict(int)
        count[0] = 1
        prefix = 0
        res = 0
        for i, num in enumerate(nums):
            prefix += num
            res += count[prefix - k]
            count[prefix] += 1
        return res
