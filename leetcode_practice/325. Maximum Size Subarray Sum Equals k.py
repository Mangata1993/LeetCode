class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        presum = collections.defaultdict(list)
        presum = {0: -1}
        prefix_sum = 0
        longest = float('-inf')
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum not in presum:
                presum[prefix_sum] = i
            if prefix_sum - k in presum:
                longest = max(longest, i - presum[prefix_sum - k])
                # print(i, presum[prefix_sum - k])
        return longest if longest != float('-inf') else 0
                
            
