class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if end - start >= duration:
                return [start, start + duration]
            else:
                if slots1[i][1] > slots2[j][1]:
                    j += 1
                else:
                    i += 1
        return []
        
        # s = list(filter(lambda slots: slots[1] - slots[0] >= duration, slots1 + slots2))
        # heapq.heapify(s)
        # while len(s) > 1:
        #     if heapq.heappop(s)[1] >= s[0][0] + duration:
        #         return [s[0][0], s[0][0] + duration]
        # return []    
        
        
