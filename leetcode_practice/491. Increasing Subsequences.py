class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(tmp, start):
            if len(tmp) >= 2 and len(nums) >= start:
                res.append(tmp[:])
            visited = {}
            for i in range(start, len(nums)):
                if tmp and nums[i] < tmp[-1]:
                    continue
                if nums[i] in visited:
                    continue
                visited[nums[i]] = True
                tmp.append(nums[i])
                backtracking(tmp, i + 1)
                tmp.pop()
            return
        backtracking([], 0)
        return res
    
    
