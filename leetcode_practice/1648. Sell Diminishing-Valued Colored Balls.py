class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        left, right = 0, max(inventory)
        total = lambda x: sum(max(0, inv - x) for inv in inventory)
        while left <= right:
            mid = (left + right) // 2
            if total(mid) < orders:
                right = mid - 1
            else:
                left = mid + 1
        print(str(left) + "," + str(mid) + "," + str(right))
        # 二分查找最后一次卖出时，球的价格是right+1。为什么？
        
        res = sum(((right + 1) + i) * (i - right) // 2 for i in inventory if i > right)
        res -= (right + 1) * (total(right) - orders)
        return res % (10**9+7)
            
        
