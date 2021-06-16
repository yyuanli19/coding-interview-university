"""
self backtracking solution, originally time out, found in the discussion that the line if len(subset) == total should be moved down to right after the recusion call
Runtime: 80 ms, faster than 64.57% of Python3 online submissions for Reconstruct Itinerary.
Memory Usage: 14.6 MB, less than 73.45% of Python3 online submissions for Reconstruct Itinerary.
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for depart, to in tickets:
            graph[depart].append(to)
        
        for depart in graph.keys():
            graph[depart].sort()
        # print(graph)
        ans = []
        self.recon("JFK", graph, ["JFK"], len(tickets)+1, ans)
        # print(ans)
        return ans[0]
    
    def recon(self, start, graph, subset, total, ans):
        if start not in graph:
            return
        des = graph[start]
        for i in range(len(des)):
            graph[start] = des[:i] + des[i+1:]
            subset += [des[i]]
            self.recon(des[i], graph, subset, total, ans)
            if len(subset) == total:
                return ans.append(subset)
            graph[start] = des
            subset.pop()


"""
euler path
found great explanation in discussion https://leetcode.com/problems/reconstruct-itinerary/discuss/709590/Python-Short-Euler-Path-Finding-O(E-log-E)-explained.
Runtime: 72 ms, faster than 93.26% of Python3 online submissions for Reconstruct Itinerary.
Memory Usage: 14.4 MB, less than 97.73% of Python3 online submissions for Reconstruct Itinerary.
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for depart, to in tickets:
            graph[depart].append(to)
        
        for depart in graph.keys():
            graph[depart].sort()
        # print(graph)
        ans = []
        self.recon("JFK", graph, ans)
        # print(ans)
        return ans[::-1]
    
    def recon(self, start, graph, ans):
        while graph[start]:
            can = graph[start].pop(0)
            self.recon(can, graph, ans)
        ans.append(start)
        
    
