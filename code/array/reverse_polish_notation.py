"""
    using the idea of stack
    Runtime: 64 ms, faster than 80.42% of Python3 online submissions for Evaluate Reverse Polish Notation.
    Memory Usage: 14.6 MB, less than 47.73% of Python3 online submissions for Evaluate Reverse Polish Notation.
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip("-+").isdigit():
                stack.append(int(i))
            else:
                num1, num2 = stack.pop(), stack.pop()
                if i == "+":
                    stack.append(num2+num1)
                if i == "*":
                    stack.append(num2*num1)
                if i == "/":
                    stack.append(int(num2/num1))
                if i == "-":
                    stack.append(num2-num1)
        return stack[-1]
        
