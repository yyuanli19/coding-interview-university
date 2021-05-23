"""
original solution, was almost right
but the add to set operation must happen first to avoid endless loop
Runtime: 64 ms, faster than 76.03% of Python3 online submissions for Keys and Rooms.
Memory Usage: 14.9 MB, less than 62.49% of Python3 online submissions for Keys and Rooms.
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited =  set()
        visited.add(0)
        self.dfs(rooms, 0, visited)
        return len(visited) == len(rooms)
    
    def dfs(self, rooms, room, visited):
        for key in rooms[room]:
            if key not in visited:
                visited.add(key)
                self.dfs(rooms, key, visited)
            

"""
had to look for solutions to finish the implementation recursively
Runtime: 64 ms, faster than 76.03% of Python3 online submissions for Keys and Rooms.
Memory Usage: 14.8 MB, less than 62.49% of Python3 online submissions for Keys and Rooms.
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        visited[0] = True
        stack = [0]
        while stack:
            idx = stack.pop()
            for key in rooms[idx]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)
        return all(visited)
