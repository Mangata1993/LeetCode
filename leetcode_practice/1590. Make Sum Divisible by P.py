class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
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
    
