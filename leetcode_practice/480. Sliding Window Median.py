class Solution:
    法一）
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        window = sorted(nums[:k])
        medians = [window[k//2] if k % 2 == 1 else (window[k//2-1]+window[k//2])/2]
        start = 0
        for i in range(k, n):
            bisect.insort(window, nums[i])
            window.pop(bisect.bisect_left(window, nums[start]))
            if k % 2 == 1:
                medians.append(window[k//2])
            else:
                medians.append((window[k//2-1] + window[k//2]) / 2)
            start += 1
        return medians
        
    法二）  
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or not k:
            return []
        lo = [] # max heap
        hi = [] # min heap
        for i in range(k):
            if len(lo) == len(hi):
                heapq.heappush(hi, -heapq.heappushpop(lo, -nums[i]))
            else:
                heapq.heappush(lo, -heapq.heappushpop(hi, nums[i]))
        ans = [float(hi[0])] if k & 1 else [(hi[0] - lo[0]) / 2.0]
        to_remove = defaultdict(int)
        for i in range(k, len(nums)): # right bound of window
            heapq.heappush(lo, -heapq.heappushpop(hi, nums[i])) # always push to lo
            out_num = nums[i-k]
            if out_num > -lo[0]:
                heapq.heappush(hi, -heapq.heappop(lo))
            to_remove[out_num] += 1
            while lo and to_remove[-lo[0]]:
                to_remove[-lo[0]] -= 1
                heapq.heappop(lo)
            while to_remove[hi[0]]:
                to_remove[hi[0]] -= 1
                heapq.heappop(hi)
            if k % 2:
                ans.append(float(hi[0]))
            else:
                ans.append((hi[0] - lo[0]) / 2.0)
        return ans
