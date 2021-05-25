"""
Had to look for solution in disucssion to complete the implementation
Runtime: 84 ms, faster than 99.84% of Python3 online submissions for All Paths From Source to Target.
Memory Usage: 15.4 MB, less than 91.41% of Python3 online submissions for All Paths From Source to Target.
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        routes = []
        self.backtrack(0, graph, [0], routes)
        return routes
    
    def backtrack(self, node, graph, route, routes):
        if node == len(graph)-1:
            return routes.append(route)
        # print(route, graph[node])
        subset = graph[node]
        for adj in graph[node]:
            self.backtrack(adj, graph, route+[adj], routes)


