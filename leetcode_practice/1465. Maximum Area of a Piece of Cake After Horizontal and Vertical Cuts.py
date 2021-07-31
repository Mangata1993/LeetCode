class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        horizontalCuts.sort()
        verticalCuts.sort()
        maxhor = max((horizontalCuts[i] - horizontalCuts[i-1]) for i in range(len(horizontalCuts)))
        maxver = max((verticalCuts[i] - verticalCuts[i-1]) for i in range(len(verticalCuts)))
        return maxhor * maxver % (10 ** 9 + 7)
