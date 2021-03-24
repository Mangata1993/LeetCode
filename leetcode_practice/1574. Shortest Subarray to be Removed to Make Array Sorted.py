class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        # if len(arr) < 2:
        #     return 0
        while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
            left += 1
        if left == len(arr) - 1:
            return 0
        
        while right > left and arr[right] >= arr[right - 1]:
            right -= 1
        print(left, right)
        
        i = 0
        j = right
        res = min(len(arr) - left - 1, right)
        while i <= left and j < len(arr):
            if arr[j] >= arr[i]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1
        return res
    
    
    
    
#         while i <= left and arr[j] >= arr[i]:            # this is a wrong solution at 1st thought
#             res = min(res, j - i - 1)
#             i += 1
            
#         # for i in range(len(arr)):
#         i = 0
#         while j < len(arr) and arr[j] < arr[i]:
#             res = min(res, j - i - 1)
#             j += 1
        
#         return res
        
        
        
            
