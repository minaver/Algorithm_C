# Topic : Data_Structur_2  _ 중앙값 구하기
#
# PyPy 3 : 1808ms
import sys

T = int(input())

for _ in range(T):  
  N = int(input())
  seq = []  # 입력받는 수열을 저장할 list
  for _ in range(N//10+1):  # 수열의 수가 10이상인 경우 N%10 +1 번 loop를 돌려 seq를 입력받는다. 
    input_tmp = list(map(int,sys.stdin.readline().rstrip().split()))
    seq.extend(input_tmp) # 계속해서 seq에 새로운 입력값을 붙혀준다.

  result = [] # 최종 결과값을 저장할 list
  for i in range(0,len(seq),2): # seq가 홀수인 경우(seq의 index가 짝수인 경우)만 중앙값을 계산해준다.
    # 중앙값 계산 부분 
    tmp = seq[:i+1] # 1. seq에서 원하는 위치까지의 요소들을 tmp로 복사
    tmp.sort()  # 2. tmp를 오름차순 정렬
    result.append(tmp[len(tmp)//2]) # 3. temp의 중앙값을 result에 append

  print((N+1)//2) # 홀수의 개수 출력

  # result를 10개로 짤라 출력
  for j in range(len(result)):  
    if j%10 == 0 and j != 0:  # result의 인덱스가 10의 배수일 경우 한번 개행
      print()
    print(result[j],end=" ")
    if j == len(result)-1:  # 마지막 인덱스에 한번 개행
      print()


      


