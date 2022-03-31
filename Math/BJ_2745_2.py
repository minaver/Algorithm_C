# Topic : MATH _ 진법 변환
# 
# int 함수 안쓰고 구현
# 알파벳 맵핑을 ASCII CODE 사용하여 int로 Mapping
# Python 3 : 68ms // PyPy 3 : 108ms

from sys import stdin

import sys 

N, B = sys.stdin.readline().split()

result = 0  # 최종 결과값 
lenght = len(N) # N 길이

for i in range(lenght): # N 길이만큼 loop
  if ord(N[(lenght-1) -i]) >= 65 and ord(N[(lenght-1) -i]) <= 90: # 계수 값이 알파벳일 경우
    coef = (ord(N[(lenght-1) -i]) - 55)
  else: # 계수 값이 그냥 숫자일 경우
    coef = int(N[(lenght-1) -i]) 

  result = result + coef * int(B)**i  

print(result)

