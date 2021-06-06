class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def count(dist):
            res = 1
            prev = position[0]
            for i in range(1, len(position)):
                if position[i] - prev >= dist:
                    res += 1
                    prev = position[i]
            print(dist, res)
            return res
        
        left, right = 0, position[-1] - position[0]
        while left <= right:
            mid = (left + right) // 2
            if count(mid) >= m:
                left = mid + 1
            else:
                right = mid - 1
        return right
