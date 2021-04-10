class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        posssum = {}
        res = 0
        for num1 in nums1:
            for num2 in nums2:
                posssum[num1 + num2] = posssum.get(num1+num2, 0) + 1
#                 if num1 + num2 not in posssum:
#                     posssum[num1 + num2] = 1
#                 else:
#                     posssum[num1 + num2] += 1
        
        for num3 in nums3:
            for num4 in nums4:
                res += posssum.get(-(num3 + num4), 0)
                # if -(num3 + num4) in posssum:
                #     res += posssum[-(num3 + num4)]
        
        return res
        
        
        
