# Topic : Data_Structure _ 괄호의 값
#
# Python 3 :
# 초기 아이디어 : 스택과 인접 비교를 사용하여 괄호를 계산하면서 올바르지 못한 괄호면 예외처리 해버린다.

import sys

line = sys.stdin.readline().rstrip()

s_num = list()
b_num = list()

s_stack = list()
b_stack = list()

s_result = []
b_result = []

i = 0
isTrue = True
# for i in range(len(line)-1):
while i < len(line)-1:
  # 1. 최소 요소들 구하기
  if line[i] == '(' and line[i+1] == ')':
    s_num.append(i)
    i += 2
    continue
  elif line[i] == '[' and line[i+1] == ']':
    b_num.append(i)
    i += 2
    continue

  # 2. 긴 요소들 구하기
  if line[i] == '(':
    s_stack.append(i)
  elif line[i] == ')':
    if len(s_stack) == 0:
      isTure = False
      break
    s_result.append([s_stack.pop(),i])
  elif line[i] == '[':
    b_stack.append(i)
  elif line[i] == ']':
    if len(b_stack) == 0:
      isTure = False
      break
    b_result.append([b_stack.pop(),i])
  i += 1

if s_stack and b_stack:
  isTrue = False
elif len(s_stack) == 0 and len(b_stack) == 0:
  isTrue = False

if isTrue == True:
  if s_stack:
    s_result.append([s_stack.pop(),i])
  elif b_stack:
    b_result.append([b_stack.pop(),i])

  sum = 0
  for s in s_num:
    sum_s = 2
    for sr in s_result:
      if sr[0] < s and s < sr[1]:
        sum_s *= 2
    for br in b_result:
      if br[0] < s and s < br[1]:
        sum_s *= 3
    sum += sum_s

  for b in b_num:
    sum_b = 3
    for sr in s_result:
      if sr[0] < b and b < sr[1]:
        sum_b *= 2
    for br in b_result:
      if br[0] < b and b < br[1]:
        sum_b *= 3
    sum += sum_b

  print(sum)
else:
  print(0)





