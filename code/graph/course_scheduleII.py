"""
solution using indegree
Runtime: 112 ms, faster than 17.12% of Python3 online submissions for Course Schedule II.
Memory Usage: 15.6 MB, less than 76.52% of Python3 online submissions for Course Schedule II.
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        sorted_schedule = []
        #make a graph
        graph = defaultdict(list)
        for child, par in prerequisites:
            graph[par].append(child)
            indegree[child] += 1
        # print(indegree)
        # compute in degree
        queque = []
        for i, course in enumerate(indegree):
            if course == 0:
                queque.append(i)
        while queque:
            course = queque.pop(0)
            sorted_schedule.append(course)
            for child in graph[course]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queque.append(child)
        if len(sorted_schedule) != numCourses:
            return []
        return sorted_schedule

"""
solution using topological sort
Runtime: 124 ms, faster than 17.12% of Python3 online submissions for Course Schedule II.
Memory Usage: 16.7 MB, less than 76.52% of Python3 online submissions for Course Schedule II.
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited = [False] * (numCourses + 1)
        recStack = [False] * (numCourses + 1)
        order =[]
        graph = defaultdict(list)
        for child, par in prerequisites:
            graph[par].append(child)
        # print(graph)
        for node in range(numCourses):
            if visited[node] == False:
                if self.isCyclicUtil(node, graph, visited, recStack, order) == True:
                    return []
        return order
    
    def isCyclicUtil(self, v, graph, visited, recStack, order):
 
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, graph, visited, recStack, order) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        order.insert(0,v)
        return False
        
