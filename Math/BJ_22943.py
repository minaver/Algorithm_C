# Topic : MATH _ 수
#
# Python 3 : 

import math
import sys

def sosu(n):
  for i in range(2,int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  return True

# K가지 숫자(K 자리수)일때 자리수당 숫자 같은지 비교 
# [구현 방식]
# num에 0~9 범위의 list 초기화
# 자리수별로 나오는 수에 해당하는 list 요소 ++
# num에 1 초과인 요소 존재시 같은 숫자가 존재한다고 판단
# 같으면 True 다르면 False
def compare(n,K):
  num = [0 for i in range(10)]
  for k in range(K):
    num[int(str(n)[k])] += 1
    
  for n in num:
    if n > 1:  
      return False
  return True


K , M = map(int,sys.stdin.readline().split())

# 공통 필요 부분
# 해당 자리수에 해당하는 소수 모두 구하기 
# e.g. K가 3이면 3자리수까지 해당하는 모든 소수 구한다(2~997)
sosu_list = list()
for i in range(2,10**K):
  if sosu(i) == True:
    sosu_list.append(i)

# print(sosu_list)

# 1번 조건
# 1. 소수 합 구하기 
# [구현 방식]
# 가능한 모든 소수합에 대해서 판별 진행
# (자리수가 K 자리수인지 확인) and (모든 자리수의 숫자가 다른지 확인)
# 다음 조건 만족시 list에 append
sosu_add = list()
for p in range(len(sosu_list)):
  for q in range(p+1,len(sosu_list)):
    add = sosu_list[p] + sosu_list[q]
    if len(str(add)) == K and compare(add,K) == True: # (자리수가 K 자리수인지 확인) and (모든 자리수의 숫자가 다른지 확인)
      sosu_add.append(add)

# 2번 조건
sosu_mod = [ sa%M for sa in sosu_add ]
max_sosu_mod = max(sosu_mod)
2
sosu_mod_list = list()
for i in range(2,max_sosu_mod):
  if sosu(i) == True:
    sosu_mod_list.append(i)

sosu_mul = list()
for p in range(len(sosu_mod_list)):
  for q in range(p,len(sosu_mod_list)):
    mul = sosu_mod_list[p] * sosu_mod_list[q]
    sosu_mul.append(mul)

result = list()
for mod in sosu_mod:
  for mul in sosu_mul:
    if mod == mul:
      result.append(mod)
      break

print(len(result))


