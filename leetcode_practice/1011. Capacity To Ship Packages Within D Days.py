class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        # need = 1                #这两句要放在while里面！因为每次换mid都是重新来过
        # curr = 0
        while left < right:
            mid = (left + right) // 2
            need = 1
            curr = 0
            for weight in weights:
                if curr + weight > mid:
                    need += 1
                    curr = weight           #这句，更新curr
                else:
                    curr += weight
            if need > D:
                left = mid + 1
            else:
                right = mid
        return left
    
    
    
