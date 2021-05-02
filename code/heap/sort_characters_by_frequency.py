"""
Runtime: 44 ms, faster than 59.50% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 16.4 MB, less than 21.78% of Python3 online submissions for Sort Characters By Frequency.
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = dict()
        for letter in s:
            dic[letter] = dic.get(letter, 0) +1
        
        freq = [(-v, k) for k, v in dic.items()]
        heapq.heapify(freq)
        # print(freq)
        # Build string
        res = []
        while freq:
            v, k = heapq.heappop(freq)
            res += [k] * -v
        return ''.join(res)

"""
use collection.counter makes the code much faster
Runtime: 32 ms, faster than 95.34% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 16.3 MB, less than 23.77% of Python3 online submissions for Sort Characters By Frequency.
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        # dic = dict()
        # for letter in s:
        #     dic[letter] = dic.get(letter, 0) +1
        dic = collections.Counter(s)
        freq = [(-v, k) for k, v in dic.items()]
        heapq.heapify(freq)
        # print(freq)
        # Build string
        res = []
        while freq:
            v, k = heapq.heappop(freq)
            res += [k] * -v
        return ''.join(res)
