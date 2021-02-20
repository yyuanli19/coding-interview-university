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
