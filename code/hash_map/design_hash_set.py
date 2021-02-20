"""
    Runtime: 152 ms, faster than 86.37% of Python3 online submissions for Design HashSet.
    Memory Usage: 18.7 MB, less than 85.12% of Python3 online submissions for Design HashSet.
"""
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.set = [[] for _ in range(self.size)]
    
    def hash_func(self, key):
        return key%1000

    def add(self, key: int) -> None:
        hashed_key = self.hash_func(key)
        if not self.contains(key):
            self.set[hashed_key].append(key)
        # print("add", key)

    def remove(self, key: int) -> None:
        hashed_key = self.hash_func(key)
        if self.contains(key):
            self.set[hashed_key].remove(key)
            # print("rem", key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashed_key = self.hash_func(key)
        return key in self.set[hashed_key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

"""
    open addressing
    Runtime: 208 ms, faster than 61.34% of Python3 online submissions for Design HashSet.
    Memory Usage: 18.9 MB, less than 70.12% of Python3 online submissions for Design HashSet.
"""
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 8
        self.size = 0
        self.set = [None]*self.capacity
        self.lf = 0.6
        
    def myhash(self, key):
        return key%self.capacity
        
    def rehash(self, key):
        return (5*key + 1) % self.capacity
    
    def table_doubling(self):
        self.capacity <<= 1
        ns = [None]*self.capacity
        for i in range(self.capacity >> 1):
            if self.set[i] and self.set[i] != "deleted":
                n = self.myhash(self.set[i])
                while ns[n] is not None:
                    n = self.rehash(n)
                ns[n] = self.set[i]
        self.set = ns

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if float(self.size)/self.capacity >= self.lf:
            self.table_doubling()
        h = self.myhash(key)
        while self.set[h] is not None:
            if self.set[h] == key:
                return
            h = self.rehash(h)
            if self.set[h] == "deleted":
                break
        self.set[h] = key
        self.size += 1
        # print("add", self.set)
        
    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        h = self.myhash(key)
        while self.set[h]:
            if self.set[h] == key:
                self.set[h] = "deleted"
                self.size -= 1
                return
            h = self.rehash(h)
        # print("rem", self.set)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        h = self.myhash(key)
        while self.set[h] is not None:
            if self.set[h] == key:
                return True
            h = self.rehash(h)
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
