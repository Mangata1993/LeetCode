class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(n-1):
            curr = res[0]
            count = 1
            tmp = ''
            for s in res[1:]:
                if s == curr:
                    count += 1
                else:
                    tmp += str(count) + str(curr)
                    curr = s
                    count = 1
            tmp += str(count) + str(curr)
            res = tmp
        return res
    
    
    
