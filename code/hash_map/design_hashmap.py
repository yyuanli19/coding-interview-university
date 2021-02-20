"""
    Runtime: 252 ms, faster than 49.76% of Python3 online submissions for Design HashMap.
    Memory Usage: 17.5 MB, less than 59.87% of Python3 online submissions for Design HashMap.
"""
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.set = [[] for _ in range(self.size)]
    
    def hash_func(self, key):
        return key%1000
    

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashed_key = self.hash_func(key)
        if not self.contains(key):
            self.set[hashed_key].append((key, value))
        else:
            self.remove(key)
            self.put(key, value)
        # print("add", self.set)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashed_key = self.hash_func(key)
        if self.contains(key):
            index = self.get_index(key)
            return self.set[hashed_key][index][1]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashed_key = self.hash_func(key)
        if self.contains(key):
            index = self.get_index(key)
            self.set[hashed_key].pop(index)

    def contains(self, key):
        hashed_key = self.hash_func(key)
        keys = [self.set[hashed_key][i][0] for i in range(len(self.set[hashed_key]))]
        return key in keys
    
    def get_index(self, key):
        hashed_key = self.hash_func(key)
        keys = [self.set[hashed_key][i][0] for i in range(len(self.set[hashed_key]))]
        return keys.index(key)
    
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""
    chaining using linked list
    Runtime: 220 ms, faster than 71.81% of Python3 online submissions for Design HashMap.
    Memory Usage: 17.6 MB, less than 46.53% of Python3 online submissions for Design HashMap.
"""
class LinkedList:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.set = [None]*self.size
    
    def hash_func(self, key):
        return key%self.size
    

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashed_key = self.hash_func(key)
        if self.set[hashed_key]:
            cur = self.set[hashed_key]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value)
                    return
                if cur.next == None:
                    cur.next = LinkedList(key, value)
                    break
                cur = cur.next
        else:
            self.set[hashed_key] = LinkedList(key, value)
 
        # print("add", self.set)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashed_key = self.hash_func(key)
        cur = self.set[hashed_key]
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
        hashed_key = self.hash_func(key)
        cur  = prev = self.set[hashed_key]
        if cur:
            if cur.pair[0] == key:
                self.set[hashed_key] = cur.next
            else:
                cur = cur.next
                while cur:
                    if cur.pair[0] == key:
                        prev.next = cur.next
                        break
                    else:
                        cur, prev = cur.next, cur

        # print("rem", self.set)
         
    
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
