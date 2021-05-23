"""
find 0 indegree
leetcode speed/memory comparison is not so accurate on this one
Runtime: 1156 ms, faster than 78.43% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
Memory Usage: 53.2 MB, less than 32.96% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
"""
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0]*n
        graph = defaultdict(list)
        for par, child in edges:
            graph[par].append(child)
            indegree[child] += 1
        
        res = []
        for i, ver in enumerate(indegree):
            if ver == 0:
                res.append(i)
        return res
        
"""
A cleaner implementation
Runtime: 1172 ms, faster than 60.48% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
Memory Usage: 53.2 MB, less than 45.26% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
"""
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set(range(n))
        for e in edges:
            if e[1] in ans:
                ans.remove(e[1])
        return list(ans)
