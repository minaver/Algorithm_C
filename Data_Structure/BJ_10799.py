# Topic : Data_Structure _ 쇠막대기
#
# PyPy 3 : 3184ms <- 겁나 오래걸림
# 초기 아이디어 :
# '('가 등장하고 ')'가 바로 나오는 경우와 그렇지 않은 경우를 구분하여
# 전자의 경우 '()'에는 레이저로 판별 후자의 경우는 쇠막대기로 판별하여 계산

import sys

line = list(sys.stdin.readline().rstrip())

pip = list()
laser = list()
stack = list()

i = 0
while i < len(line):
  # 1. find ()
  if line[i] == '(' and line[i+1] == ')':
    laser.append(i)
    i += 2
    continue

  # 2. find 쇠막대기
  if line[i] == '(':
    stack.append(i)
    # print(stack)
  else:
    pip.append([stack.pop(),i])
  
  i += 1

# print(raser)
# print(pip)

count = 0
for p in pip:
  for r in laser:
    if p[0] < r and p[1] > r:
      count += 1
  count += 1

print(count)






