class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.map = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucketCode = key % self.size
        if self.map[bucketCode] == None:
            self.map[bucketCode] = ListNode(key, value)
        else:
            cur = self.map[bucketCode]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value)     # update
                    return
                if cur.next == None:        # 想象成每个listnode都是一对(key, value)，对于对之间有next指针
                    cur.next = ListNode(key, value)
                    break
                cur = cur.next
            
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucketCode = key % self.size
        cur = self.map[bucketCode]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucketCode = key % self.size
        cur = prev = self.map[bucketCode]
        if not cur:
            return
        if cur.pair[0] == key:
            self.map[bucketCode] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next
            
    

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

      
