class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dic1 = Counter(num * num for num in nums1)
        dic2 = Counter(num * num for num in nums2)
        res = 0
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                p = nums2[i] * nums2[j]
                res += dic1[p]
        
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                p = nums1[i] * nums1[j]
                res += dic2[p]
        
        return res
     
        
        
        
