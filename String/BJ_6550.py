# Topic : String _ 부분 문자열
#
# Python 3 : 92ms
# 계속 입력 받는 문제인지 모르고 계속 실패 떠서 한참 헤맸다.

import sys

def checkPartOfString(S,T):
  last_index = 0

  for j in range(len(S)): # S loop
    for i in range(last_index,len(T)):  # T loop
      if S[j] == T[i]:  # 같은 문자를 찾았을때 
        # print(i,":",T[i])
        if j == len(S) -1:  # 마지막 문자까지 모두 찾았을때 True Return
          return True

        last_index = i+1  # T에서 찾은 문자의 index를 저장 (추후 이 인덱스보다 큰 부분부터 loop 돈다.)
        break

      if i == len(T)-1: # 만약 S의 다음 문자를 T에서 찾는데(loop) 끝까지 없다면 부분 문자열이 아닌것!
        return False


while True:
  try :
    s , t = sys.stdin.readline().rstrip().split()
    if checkPartOfString(s,t) == True:
      print("Yes")
    else:
      print("No")
  except: 
    break

