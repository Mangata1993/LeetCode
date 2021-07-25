class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        
        num = [int(char) for char in num]
        # print(num)
        replace = False
        for i in range(len(num)):
            if num[i] < change[num[i]]:
                num[i] = change[num[i]]
                if not replace:
                    replace = True
                # print(res)
            elif num[i] == change[num[i]]:
                continue
            elif replace:
                break
        
        res = [str(num) for num in num]
        return ''.join(res)
