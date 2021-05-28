class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
# 假设 nums 的和除以 P，余数是 mod，如果 mod == 0，答案就是 0。如果 mod != 0，答案变成了找原数组中的最短连续子数组，使得其数字和除以 P，余数也是 mod。
# 由于是求解连续子数组和的问题，很容易想到使用前缀和。
# 我们可以扫描一遍整个数组，计算到每个元素的前缀和。
# 假设当前前缀和除以 P 的余数是 curmod，为了找到一段连续子数组对 P 的余数是 mod，我们需要找到一段前缀和，对 P 的余数是 targetmod。其中 targetmod 的求法是：
# 如果 curmod >= mod，很简单：targetmod = curmod - mod；
# 如果 curmod < mod，我们需要加上一个 P：targetmod = curmod - mod + P；
# 这样，我们可以保证，当前前缀和减去目标前缀和，剩余的数组对 P 的余数是 mod。我们只需要找最短的这样的数组就好。

        cur_sum = 0
        mod = sum(nums) % p
        if mod == 0:
            return 0
        mod_dict = {0:-1}
        res = float('inf')
        for i, num in enumerate(nums):
            cur_sum += num
            cur_mod = cur_sum % p
            target_mod = cur_mod - mod if cur_mod >= mod else cur_mod + p - mod
            if target_mod in mod_dict:
                res = min(res, i - mod_dict[target_mod])
            mod_dict[cur_mod] = i
                
        return res if res != len(nums) else -1
    
