class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        lst = preorder.split(',')
        print(lst)
        for i in lst:
            slots -= 1
            if slots < 0:
                return False
            if i.isnumeric():
                slots += 2
        return slots == 0
    
     
