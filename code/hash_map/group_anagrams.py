"""
    Runtime: 88 ms, faster than 95.79% of Python3 online submissions.
    Memory Usage: 17.6 MB, less than 59.67% of Python3 online submissions.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for word in strs:
            key = ''.join(sorted(word))
            res[key] = res.get(key, []) + [word]
        # print(res)
        return res.values()
        
