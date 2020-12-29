"""
    self-solution, verly inefficient, and it could potentially lead to stack overflow problem
    Runtime: 936 ms, faster than 13.04% of Python3 online submissions for Fibonacci Number.
    Memory Usage: 14.3 MB, less than 6.21% of Python3 online submissions for Fibonacci Number.
"""
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            #final_sum = self.fib(n-1) + self.fib(n-2)
            return self.fib(n-1) + self.fib(n-2)

"""
    one of official solutions, that saves the tmp results in a dict
    Runtime: 32 ms, faster than 57.90% of Python3 online submissions for Fibonacci Number.
    Memory Usage: 14.1 MB, less than 55.20% of Python3 online submissions for Fibonacci Number.
"""
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.memorize(n)

    def memorize(self, n) -> {}:
        cache = {0:0, 1:1}
        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, n+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n]
        
"""
    one of official solutions, that saves the tmp results in a dict and uses recursion
    Runtime: 28 ms, faster than 82.35% of Python3 online submissions for Fibonacci Number.
    Memory Usage: 14.4 MB, less than 6.21% of Python3 online submissions for Fibonacci Number.
"""
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        self.cache = {0:0, 1:1}
        return self.memorize(n)

    def memorize(self, n) -> {}:
        if n in self.cache.keys():
            return self.cache[n]
        self.cache[n] = self.memorize(n-1) + self.memorize(n-2)
        return self.memorize(n)

"""
    matrix multiplication, worth reading many times
    Runtime: 32 ms, faster than 57.90% of Python3 online submissions for Fibonacci Number.
    Memory Usage: 14.4 MB, less than 6.21% of Python3 online submissions for Fibonacci Number.
"""
class Solution:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N

        A = [[1, 1], [1, 0]]
        self.matrix_power(A, N-1)

        return A[0][0]

    def matrix_power(self, A: list, N: int):
        if (N <= 1):
            return A

        self.matrix_power(A, N//2)
        self.multiply(A, A)
        B = [[1, 1], [1, 0]]

        if (N%2 != 0):
            self.multiply(A, B)

    def multiply(self, A: list, B: list):
        x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        w = A[1][0] * B[0][1] + A[1][1] * B[1][1]

        A[0][0] = x
        A[0][1] = y
        A[1][0] = z
        A[1][1] = w
