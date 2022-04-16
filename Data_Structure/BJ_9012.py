# Topic : Data_Structure _ 괄호
#
# PyPy 3 : 112 ms
# 초기 아이디어 : 스택 이용

import sys

N = int(input())
result = list()

for n in range(N):
  line = sys.stdin.readline().rstrip()

  stack = list()
  check = True

  for i in range(len(line)):
    if line[i] == '(':  # ( 등장시 스택에 하나 추가
      stack.append(1)
    elif line[i] ==')': # ) 등장시 스택에서 하나 pop
      if len(stack) == 0: # 만약 stack에 아무것도 없다면 not VPS
        check = False
        break
      else:
        stack.pop()

  # print("i :",i,"stack :",stack)
  # 마지막 글자까지 확인을 다함 and stack에 남은 '('가 없음 and 중간에 ')' 등장시 stack에 사용할 수 있는 '('가 없는 경우가 없음 일때만 YES!
  if i == len(line)-1 and len(stack) == 0 and check == True:
    result.append("YES")
  else:
    result.append("NO")
  

for r in result:
  print(r)

