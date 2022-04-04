# Topic : MATH _ 폰 호석만
#
# Python 3 : 68ms(11/24)
import sys

a , b = sys.stdin.readline().split()

a = a.upper()
b = b.upper()

max_a = max(a)
max_b = max(b)

# a,b 각각의 최소 진법 구하기
# ef에 경우 16진법(f)아래의 진법으로는 표현이 불가하다
if ord(max_a) > 57: # 10진법 이상일시 (알파벳값 등장)
  min_a = int(ord(max_a)-54) # a가 가능한 최소 진법 
elif ord(max_a) > 48:  # 10진법 이하일시 (알파벳값 미등장)
  min_a = int(max_a)+1
else: # max_a == 0일시
  min_a = 2 

if ord(max_b) > 57:  # 10진법 이상일시 (알파벳값 등장)
  min_b = int(ord(max_b)-54) # b가 가능한 최소 진법
elif ord(max_b) > 48:  # 10진법 이하일시 (알파벳값 미등장)
  min_b = int(max_b)+1
else: # max_a == 0일시
  min_b = 2 

count = 0 # 여러 경우의 수가 나오는지 확인하는 var
for i in range(min_a,37): # a가 가능한 진법들
  for j in range(min_b,37): # b가 가능한 진법들
    if i == j:  # A != B
      continue

    if int(a,i) == int(b,j):  # 각각의 경우에서 a,b가 같아지는 진법이 있는지 확인
      if int(a,i) >= 2**63: # 0 ≤ X < 2**63
        continue

      if count == 1:  # 만약 이미 같아지는 진법이 존재했다면 Multiple
        print("Multiple")
        break
      
      # 결과값 저장
      result_X = int(a,i)
      result_A = i
      result_B = j

      count = count + 1
  
  if count != 0:
    break

if count == 0: # 가능한 진법이 없는 경우 
  print("Impossible")
elif count != 1: # 가능한 진법이 단하나인 경우 
  print(result_X,result_A,result_B,sep=" ")

