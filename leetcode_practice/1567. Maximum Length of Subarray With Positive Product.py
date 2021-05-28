class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # count_neg, first_zero, first_neg = 0, -1, float('inf')
        # res = 0
        # for i, num in enumerate(nums):
        #     if num == 0:      # 遇到0时状态初始化
        #         count_neg, first_zero, first_neg = 0, i, float('inf')
        #     elif num < 0:
        #         count_neg += 1
        #         first_neg = min(first_neg, i)       #考虑到first_neg可能会重置，所以不是每次first_neg都一定比i小
        #     if count_neg % 2 == 0:
        #         res = max(res, i - first_zero)
        #     else:         # 遇到的负数是奇数个，则最大长度为当前坐标减去到第一个遇到的负数的坐标
        #         res = max(res, i - first_neg)
        # return res
        
        # 法二） DP
        # 定义两个数组 positive 和 negative，其中 positive[i] 表示以下标 i结尾的乘积为正数的最长子数组长度，negative[i] 表示乘积为负数的最长子数组长度
        pos_dp, neg_dp = [0] * len(nums), [0] * len(nums)
        pos_dp[0] = int(nums[0] > 0)
        neg_dp[0] = int(nums[0] < 0)
        for i in range(1, len(nums)):
            if nums[i] == 0:
                pos_dp[i], neg_dp[i] = 0, 0
            elif nums[i] > 0:
                pos_dp[i] = pos_dp[i-1] + 1     #不用判断前面的，因为即使前面的不存在，当前这个数可以直接+1
                neg_dp[i] = neg_dp[i-1] + 1 if neg_dp[i-1] else 0   #必须前面有负数才能在那基础上+1，没有负数存在的话直接0
            else:
                pos_dp[i] = neg_dp[i-1] + 1 if neg_dp[i-1] else 0
                neg_dp[i] = pos_dp[i-1] + 1
        return max(pos_dp)          #注意这里不是return dp array的最后一个值了！而是array里的最大值

