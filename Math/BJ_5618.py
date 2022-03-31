# Topic : MATH_ 공약수
# Result : pypy3 : 1240ms / python3에서는 시간 초과 

n = int(input())
list = list()

if n == 2:
  p,q = map(int,input().split())

  for i in range(1,min(p,q)+1):
    if p%i == 0 and q%i == 0:
      list.append(i)

else:
  p,q,r = map(int,input().split())

  for i in range(1,min(p,q,r)+1):
    if p%i == 0 and q%i == 0 and r%i ==0:
      list.append(i)

[print(i) for i in list]

