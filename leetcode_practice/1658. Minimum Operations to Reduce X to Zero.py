class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        res = 0
        cursum = 0
        dic = {0:-1}
        if target == 0:
            return len(nums)
        for i, num in enumerate(nums):
            cursum += num
            if cursum - target in dic:
                res = max(res, i - dic[cursum - target])
            if cursum not in dic: 
                dic[cursum] = i
        print(res)
        return len(nums) - res if res else -1
