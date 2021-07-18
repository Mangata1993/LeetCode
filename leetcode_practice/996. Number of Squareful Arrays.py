class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        self.count = set()
        def squareful(a, b):
            return pow(int(sqrt(a + b)), 2) == a + b
        
        def backtracking(start):
            # print(start, nums)
            if start == len(nums):
                self.count.add(str(nums))
                # print(self.count)
            for i in range(start, len(nums)):
                # print(start)
                if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    continue
                nums[start], nums[i] = nums[i], nums[start]
                if start == 0 or squareful(nums[start - 1], nums[start]):
                    # 这边最关键的就是要加上start == 0，不然的话start-1就是最后一个数，所以错了。所以要把start==0单独拎出来
                    backtracking(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        nums.sort()
        backtracking(0)
        return len(self.count)
        
        
