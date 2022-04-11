# Topic : String _ 이 구역의 승자는 누구야?!
#
# PyPy 3 : 216ms
# 아니 다른 사람들 엄청 쉽게 풀었네,,
# 그냥 문제 나온대로 무지성으로 구현했는데 다른 사람들은 전체 합 mod 10 연산으로 그냥 쉽게 구했다.
# 문제를 풀때 뭐 문제가 접근하는 방식으로 사고하는건 좋지만 좀더 멀리서 직관적으로 바라보는 시각도 필요함!

import sys

def calc(input):
  if len(input) == 1: # 들어온 input의 길이가 1인 경우 계산이 모두 완료된 것!
    if input[0]%2 != 0: # 홀수일 경우
      print("I'm a winner!")  
    else: # 짝수일 경우
      print("You're the winner?")
    return 0
  
  next_input = list() # 다음 calc 함수에 보낼 input list
  for i in range(0,len(input),2): # +2씩 증가하여 loop 수행
    if i == len(input)-1: # 만약 홀수개의 input에서 마지막 input값을 참조할 경우
      next_input.append(input[i]) # 그냥 그 값을 다음 input list에 넣어준다.
    else: # 나머지의 경우 i, i+1 인 요소들을 더한 값에 mod 10 값을 넣어준다.
      next_input.append((input[i]+input[i+1])%10)

  calc(next_input)  # 다음 calc 재귀 호출


alp = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]

input = sys.stdin.readline().rstrip()

num_input = list()
for i in input: # 문자값을 미리 정의된 alp에 해당하는 값으로 맵핑
  num_input.append(alp[ord(i)-65])

calc(num_input)




