# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means the expression 
# would always evaluate to a result, and there will not be any division by zero operation.

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
import math
def evalRPN(tokens):
    stack = []
    for i in tokens:
        if i.isnumeric() or (len(i) > 1 and i[0] == '-'):
            stack.append(int(i))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if i == '+':
                new = num1 + num2
                stack.append(new)
            elif i == '*':
                new = num1 * num2
                stack.append(new)
            elif i == "-":
                new = num1 - num2
                stack.append(new)
            else:
                new = num1 / num2
                new = math.floor(new) if new >= 0 else math.ceil(new)
                stack.append(new)
    return int(stack[0])

# print(evalRPN(["2","1","+","3","*"]))
# print(evalRPN(["4","13","5","/","+"]))
# print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(evalRPN(["4","13","5","/","+"]))

# print((6/-132).tofixed(0))