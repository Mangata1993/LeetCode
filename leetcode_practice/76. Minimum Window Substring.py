class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        needcnt = len(t)                        # t can have duplicates
        start, end = 0, -1
        i = 0
        for j, char in enumerate(s):
            if need[char] > 0:
                needcnt -= 1
            need[char] -= 1
            # print(need)
            if needcnt == 0:                    # match all chars
                while i < j and need[s[i]] < 0:         # remove chars to find the real start 
                    need[s[i]] += 1
                    i += 1
                if end == -1 or j - i < end - start:
                    start, end = i, j       # update the result
                need[s[i]] += 1        # now we can move the left. make sure the first appearing char satisfies need[char]>0
                needcnt += 1                # we missed this first char, so add missing by 1
                i += 1                 # all these three lines are for the same purpose which is to move left to the first position that doesn't meet the requirement(need[s[i]]>=0)
        return s[start : end + 1]
   
  
  
  
