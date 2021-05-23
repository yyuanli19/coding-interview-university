"""
using topological sort
73.65%
41.34%
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * (numCourses + 1)
        recStack = [False] * (numCourses + 1)
        graph = defaultdict(list)
        for child, par in prerequisites:
            graph[par].append(child)
        # print(graph)
        for node in range(numCourses):
            if visited[node] == False:
                if self.isCyclicUtil(node, graph, visited, recStack) == True:
                    return False
        return True
    
    def isCyclicUtil(self, v, graph, visited, recStack):
 
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, graph, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False
