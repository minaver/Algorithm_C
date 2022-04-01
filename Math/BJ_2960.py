# Topic : MATH _ 에라토스테네스의 체
#
# PyPy 3 : 104ms
import sys

def eratos(N,K):
  list = [ 1 for i in range(N+1) ]  # 0부터 N까지 모든 정수를 갖는 list 생성 (1로 초기화) 

  count = 0 # K번째로 지워지는 수가 무엇인지 확인하는 var
  for i in range(2,N+1):  
    if list[i] == 0:  # list가 이미 0으로 초기화 되어 있으면 continue
      continue
    
    num = 1 # i를 배수해줄 num (P의 배수)
    while i*num <= N: # P의 배수가 N 이하일 경우 loop
      if list[i*num] != 0:  # list가 이미 0으로 초기화 되어 있으면 continue
        list[i*num] = 0 # list[P의 배수] 를 0으로 지움

        count = count + 1 # count++
        if count == K:  # count가 K와 동일시 해당 값 출력
          print(i*num)

      num = num + 1
    
  return list

N, K = map(int,sys.stdin.readline().split())

eratos(N,K)


