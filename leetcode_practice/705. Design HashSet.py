class ListNode:
    def __init__(self, key, next):
        self.key = key
        self.next = next
        
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [None] * self.size

    def add(self, key: int) -> None:            # key就是value
        bucketCode = key % self.size
        cur = self.buckets[bucketCode]
        if not cur:
            self.buckets[bucketCode] = ListNode(key, None)
            return
        if cur.key == key:
            return
        while cur:
            if cur.key == key:
                return 
            if not cur.next:
                cur.next = ListNode(key, None)
                return
            if cur.next:
                cur = cur.next
        return

    def remove(self, key: int) -> None:
        bucketCode = key % self.size
        cur = self.buckets[bucketCode]
        if not cur:
            return
        if cur.key == key:
            self.buckets[bucketCode] = cur.next
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucketCode = key % self.size
        cur = self.buckets[bucketCode]
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False
    
    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

  
