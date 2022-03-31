# Topic : MATH _ 더하기 사이클
#
# PyPy 3 : 112ms

import sys

N = int(sys.stdin.readline())
origin = N  # 최초 N 값 저장
count = 0

while True:
  if N < 10: # 한자리 수 일 경우 "NN" 형태로 도출
    N = 11*N
  else:
    sum = N//10 + N%10  # 10의 자리수 숫자와 1의 자리수 숫자를 더함
    N = (N%10)*10 + sum%10  # N의 1의 자리수 가 10의 자리로 sum의 1의 자리수가 1의 자리로

  count = count + 1

  if origin == N:
    break


print(count)

  
