# Topic : Data_Structure _ 쇠막대기 2
#
# PyPy 3 :
import sys 

razor = list(sys.stdin.readline())
stack = []

sum = 0

for i in range(len(razor)):
    if razor[i] == '(':
        stack.append('(')
    else:
        if razor[i - 1] == '(':
            stack.pop()
            sum += len(stack)
        else:
            stack.pop()
            sum += 1
print(sum)