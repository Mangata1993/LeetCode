class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def getsum(arr, t):
            sumarr = sum(t if num >= t else num for num in arr)
            return sumarr
        
        left, right = 1, max(arr)
        while left <= right:
            mid = (left + right) // 2
            if getsum(arr, mid) == target:
                return mid
            elif getsum(arr, mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        if abs(getsum(arr, left) - target) < abs(getsum(arr, right) - target):
            return left
        return right
    
