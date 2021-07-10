class Solution:

    def __init__(self, w: List[int]):
        self.presums = []
        self.presum = 0
        for weight in w:
            self.presum += weight
            self.presums.append(self.presum)
        

    def pickIndex(self) -> int:
        target = self.presum * random.random()
        left, right = 0, len(self.presums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == self.presums[mid]:
                return mid
            elif target < self.presums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
