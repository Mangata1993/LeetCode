class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                start = i-1
                break
        end = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] < nums[i-1]:
                end = i
                break
        if start == end:
            return 0
        min_num = min(nums[start:end+1])
        max_num = max(nums[start:end+1])
        print(start, end)
        l, r = start, end
        while l > 0 and min_num < nums[l-1]:
            l -= 1
        while r < len(nums) - 1 and max_num > nums[r+1]:
            r += 1    
        print(l, r)
        return r - l + 1
    
#     n = len(nums)
#         start = 0
#         end = n - 1
#         for i in range(n):
#             if nums[i] >= nums[start]:
#                 start = i
#             else:
#                 break
#         for i in range(n-1, start, -1):
#             if nums[i] <= nums[end]:
#                 end = i
#             else:
#                 break
#         if start == end:
#             return 0

#         # O(n)
#         min_num = min(nums[start:end+1])
#         max_nums = max(nums[start:end+1])
        
#         left, right = start, end
#         for i in range(start, -1, -1):
#             if nums[i] > min_num:
#                 left = i
#         for i in range(end, n):
#             if nums[i] < max_nums:
#                 right = i

#         return right - left + 1

# 作者：lfywork
# 链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/ke-neng-shi-onde-jie-fa-by-lfywork-99vp/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    
# #         right_ptr = 0
# #         big = nums[0]
# #         for i in range(len(nums)):
# #             if nums[i] < big: 
# #                 # a number smaller than what we have seen -> need sorting
# #                 right_ptr = i
# #             else:
# #                 big = nums[i]
        
# #         # Find left limit of the subarray. Traverse array from right to left
# #         left_ptr = 0
# #         small = nums[-1]
# #         for i in reversed(range(len(nums))):
# #             if nums[i] > small: 
# #                 # a number bigger than what we have seen -> need sorting
# #                 left_ptr = i
# #             else:
# #                 small = nums[i]
# #         print(right_ptr, left_ptr)       
# #         if right_ptr == left_ptr: return 0
# #         return right_ptr - left_ptr + 1
