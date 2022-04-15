# Topic : Data_Structure _ 스택
#
# Python 3 : 80 ms
# 입력시 .split()을 써서 cmd와 정수를 따로 입력 받았어도 괜찮았을듯 하다!

import sys

def push(stack,X):
  stack.append(X)
  return stack

def pop(stack):
  if len(stack) == 0:
    return -1
  else:
    tmp = stack[-1]
    del stack[-1]
    return tmp

def size(stack):
  return len(stack)

def empty(stack):
  if len(stack) == 0:
    return 1
  else:
    return 0

def top(stack):
  if len(stack) == 0:
    return -1
  else:
    return stack[-1]

N = int(sys.stdin.readline())

stack = list()
for n in range(N):
  cmd = sys.stdin.readline().rstrip()
  if cmd.find("push") != -1:
    push(stack,int(cmd[5:]))
  elif cmd.find("top") != -1:
    print(top(stack))
  elif cmd.find("size") != -1:
    print(size(stack))
  elif cmd.find("empty") != -1:
    print(empty(stack))
  elif cmd.find("pop") != -1:
    print(pop(stack))

