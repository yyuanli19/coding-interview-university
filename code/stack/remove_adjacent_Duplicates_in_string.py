"""
    Runtime: 92 ms, faster than 38.79% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
    Memory Usage: 17.2 MB, less than 10.83% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for letter in s:
            count = 1
            if stack and stack[-1][1] == letter:
                count += stack[-1][0]
            stack.append((count, letter))
            if stack and stack[-1][0] == k:
                for i in range(k):
                    stack.pop()
            # print(letter, stack)
        final_s = ""
        for j in stack:
            final_s+=j[1]
        return final_s

# a great solution: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/392933/JavaC%2B%2BPython-Two-Pointers-and-Stack-Solution
