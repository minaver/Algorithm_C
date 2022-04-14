# Topic : Data_Structure _ 요세푸스 문제
#
# PyPy 3 : 116ms

import sys

N , K = map(int,sys.stdin.readline().split())

yoseps = [i+1 for i in range(N)]  # 1~N 의 list 생성 
result = list() # 결과를 저장할 list

i = 0 # yoseps list를 돌아다닐 index
while len(yoseps) != 0: # yoseps list의 모든 요소가 사라져 길이가 0이 될때까지 loop 
  i = (i+K-1) % len(yoseps) # * 직전 index 위치에서 K만큼 이동(+K-1)후 list의 길이로 mod 연산(인덱스 넘어가면 리스트 앞쪽으로 전환)
  result.append(yoseps[i])  # 해당 요소를 result에 저장 후
  del yoseps[i] # yoseps list에서는 없애준다.

# < ~ > 형식으로 만들어준다.
result = str(result)
result = result.replace('[','<')  
result = result.replace(']','>')
print(result)

