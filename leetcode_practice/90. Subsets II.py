class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(tmp, start):
            res.append(tmp[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                tmp.append(nums[i])
                backtracking(tmp, i + 1)
                tmp.pop()
            
        nums.sort()    
        backtracking([], 0)
        return res
        
        
        
      
