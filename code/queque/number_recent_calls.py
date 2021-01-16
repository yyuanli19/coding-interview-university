"""
    self solution that used array
    Runtime: 532 ms, faster than 21.22% of Python3 online submissions for Number of Recent Calls.
    Memory Usage: 19.1 MB, less than 47.45% of Python3 online submissions for Number of Recent Calls.
"""
class RecentCounter:

    def __init__(self):
        self.request = []
        

    def ping(self, t: int) -> int:
        self.request.append(t)
         for i, r in enumerate(self.request):
             if r>=t-3000:
                 self.request = self.request[i:]
                 break
         # print(self.request)
        return len(self.request)

"""
    the above solution is bad because array has to constantly reallocating memory
    offcially solution uses queque which is drastically faster
    Runtime: 268 ms, faster than 98.04% of Python3 online submissions for Number of Recent Calls.
    Memory Usage: 19 MB, less than 47.45% of Python3 online submissions for Number of Recent Calls.
"""
class RecentCounter:

    def __init__(self):
        self.request = deque()
        

    def ping(self, t: int) -> int:
        self.request.append(t)
        # for i, r in enumerate(self.request):
        #     if r>=t-3000:
        #         self.request = self.request[i:]
        #         break
        # # print(self.request)
        while self.request[0] < t-3000:
            self.request.popleft()
        return len(self.request)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
