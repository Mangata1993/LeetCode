class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) // 2
            if sum(ceil(num / mid) for num in nums) > threshold:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
     # at the end of loop, left > right,
        # compute_sum(right) > threshold
        # compute_sum(left) <= threshold
        # --> return left
 
