from functools import cmp_to_key
class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         # nums = [str(num) for num in nums]
#         nums = list(map(str, nums))
#         print(nums)
#         nums.sort(key = cmp_to_key(lambda x, y: int(y+x) - int(x+y)))
#         return ''.join(nums).lstrip('0') or '0'
    
    
    #   def largestNumber(self, num):
    #     num = [str(x) for x in num]
    #     num.sort(cmp=lambda x, y: cmp(y+x, x+y))
    #     return ''.join(num).lstrip('0') or '0'
    
    # def compare(x, y): return int(y+x) - int(x+y)
    #     nums = sorted(map(str, nums), key=cmp_to_key(compare))
    #     return "0" if nums[0]=="0" else "".join(nums)
    
     # from functools import cmp_to_key
     #    temp = list(map(str,nums))
     #    temp.sort(key = cmp_to_key(lambda x,y:int(x+y)-int(y+x)),reverse = True )
     #    return ''.join(temp if temp[0]!='0' else '0')
    def largestNumber(self, nums):
        self.quickSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums)))) 

    def quickSort(self, nums, l, r):
        if l >= r:
            return 
        pos = self.partition(nums, l, r)
        self.quickSort(nums, l, pos-1)
        self.quickSort(nums, pos+1, r)

    def partition(self, nums, l, r):
        low = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
