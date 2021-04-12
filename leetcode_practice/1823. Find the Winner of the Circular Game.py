class Solution:
    # [1,2,3,4,5]
    # [1,2,3,4,5,6]
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1: 
            return 1
        if k == 1:
            return n
        lst = [i for i in range(1, n + 1)]
        start = 0
        while len(lst) > 1:
            start = (start + k - 1) % len(lst)  # 0,1;2;3
            del lst[start]
        return lst[0]
