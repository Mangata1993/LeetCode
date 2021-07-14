class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) // k
        if target != sum(nums) / k:
            return False
        nums.sort()
        if nums[-1] > target:
            return False
        visited = [False] * len(nums)
        def dfs(begin, curSum, k):
            if k == 1:          # k只剩一个的话，剩下值肯定=target。剪枝
                return True
            if curSum == target:
                return dfs(len(nums) - 1, 0, k - 1)     # 找到了一个组合,还有k-1个.
            for i in range(begin, -1, -1):
                if visited[i]:
                    continue
                if curSum + nums[i] > target:
                    continue
                visited[i] = True       # 添加元素nums[i]
                if dfs(i - 1, curSum + nums[i], k):
                    return True     # 如果添加这个元素后，完成了题目要求，就return true.
                visited[i] = False
                while i > 0 and nums[i-1] == nums[i]:
                    i -= 1
            return False
        
        return dfs(len(nums) - 1, 0, k)
            
   
