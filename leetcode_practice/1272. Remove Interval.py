class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        # res = []
        # remove_start, remove_end = toBeRemoved
        # for start, end in intervals:
        #     if end < remove_start or start > remove_end:
        #         res.append([start, end])
        #     else:
        #         if start < remove_start:
        #             res.append([start, remove_start])
        #         if end > remove_end:
        #             res.append([remove_end, end])
        # return res                            #Approach 1
        res = []
        remove_start, remove_end = toBeRemoved
        for start, end in intervals:
            a = remove_start - start
            b = end - remove_end
            if remove_start > start:
                res.append([start, min(remove_start,end)])
            if end > remove_end:
                res.append([max(start,remove_end), end])
        return res              #Approach 2
      
      
      
      
