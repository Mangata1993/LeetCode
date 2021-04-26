class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        cnt = unique = 1
        res = 0
        for i in range(1, len(word)):
            if word[i] >= word[i-1]:
                cnt += 1
                if word[i] > word[i-1]:
                    unique += 1      
            else:
                cnt = unique = 1
            if unique == 5:
                res = max(res, cnt)
        return res
    
   
