class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # for i, num in enumerate(citations):
        #     if len(citations) - i <= num:
        #         return len(citations) - i
        # return 0
        
        n = len(citations)
        # left, right = 0, n - 1
        # while left <= right:
        #     pivot = (left + right) // 2
        #     if citations[pivot] == n - pivot:
        #         return n - pivot
        #     elif citations[pivot] > n - pivot:
        #         right = pivot - 1
        #     else:
        #         left = pivot + 1
        # return n - left
        
        for i in range(n, 0, -1):
            if citations[n - i] >= i:
                return i
        return 0
                
            
