# Topic : Data_Structure _ 괄호의 값
#
# Python 3 : 124ms

import sys

line = sys.stdin.readline().rstrip()

# '(' 등장시 1 
# '[' 등장시 2
stack = list()

sum = 0
i = 0
isTrue = True
while i < len(line)-1:
  # 1. 최소 요소가 등장하면 그동안 stack에 쌓인 것들을 확인하여 계산
  # '(' 등장시
  if line[i] == '(':
    if line[i+1] == ')':
      tmp_sum = 2
      for s in stack:
        if s == 1:  # '('
          tmp_sum *= 2
        elif s == 2:  # '['
          tmp_sum *= 3
      sum += tmp_sum
      i += 2
    else:
      stack.append(1)
      i += 1
  # '[' 등장시
  elif line[i] == '[':
    if line[i+1] == ']':
      tmp_sum = 3
      for s in stack:
        if s == 1:  # '('
          tmp_sum *= 2
        elif s == 2:  # '['
          tmp_sum *= 3
      sum += tmp_sum
      i += 2
    else:
      stack.append(2)
      i += 1
  # ')' 등장시
  elif line[i] == ')':
    i += 1
    if len(stack) == 0 or stack.pop() != 1:
      isTrue = False
      break
  # ']' 등장시
  elif line[i] == ']':
    i += 1
    if len(stack) == 0 or stack.pop() != 2:
      isTrue = False
      break

# [올바른 괄호열인지 확인]
# 마지막 인덱스 확인
if i == len(line)-1:
  # print(line[i])
  # print(stack)
  if len(stack) != 1:
    isTrue = False
  elif line[i] == ')' and stack.pop() != 1:
    isTrue = False
  elif line[i] == ']' and stack.pop() != 2:
    isTrue = False

# 마지막에 ()나 []가 오는경우
if i == len(line):
  if len(stack) != 0:
    isTrue = False
  
if isTrue == True:
  print(sum)
else:
  print(0)