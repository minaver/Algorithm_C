# Topic : Data_Structure _ 스택 수열
#
# PyPy 3 : 220ms

import sys

# 준비물
N = int(sys.stdin.readline()) 

input = list()   # 사용자가 입력할 수열 list
stack = list()   # stack 저장에 사용할 stack
result = list()  # +, - 의 결과가 들어갈 list
temp = list([ N-n for n in range(N)]) # 1 ~ N까지로 초기화한 stack 
isPossible = True # 만약 중간에 NO 상황이 생기면 False로 분기

# 사용자로부터 input 받기
for _ in range(N):
  input.append(int(sys.stdin.readline()))


for i in input:
  # [1] input에서 원하는 값이 나올때까지 temp의 수를 stack에 넣어준다. ex) 4가 필요한 경우면 temp의 수들을 차례로 stack에 push하는 과정
  # 1) stack에 아무것도 없을때
  # 2) input값이 stack 맨 위 값고 다를때 
  if len(stack) == 0 or i != stack[-1]:
    # [2-1] 다음 조건을 만족하면 temp의 수들을 차례로 stack에 push한다.
    # 1) temp의 길이가 0이 아닐때
    # 2) temp에 원하는 i 값이 포함되어 있을때
    if len(temp) != 0 and i >= temp[-1]: 
      while len(temp) != 0 and i != temp[-1]:
        stack.append(temp.pop())
        result.append('+')
      # 마지막 temp 값이 결론적으로 stack 들어가야할 값이므로 while 후 한번더 push 해준다.
      stack.append(temp.pop())
      result.append('+')
    # [2-2] 만약 위 조건을 만족하지 않는다면 불가능한 경우이다.
    else:
      isPossible = False
      break

  # [3] input 값과 stack 맨위 값이 동일시 pop 진행
  if i == stack[-1]:
    stack.pop()
    result.append('-')
    continue

# [4] 결과 출력
if isPossible == False:
  print("NO")
else:
  for r in result:
    print(r)

