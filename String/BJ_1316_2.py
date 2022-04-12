# Topic : String _ 그룹 단어 체커
#
# PyPy 3 :
import sys

N = int(sys.stdin.readline())
count = N # count는 N으로 초기화 한후 이후 그룹 단어가 아닌 아이들을 하나씩 빼줄거다!

for n in range(N):
  word = sys.stdin.readline()
  for i in range(0,len(word)-1):  # word index 0 ~ (마지막-1) 까지 비교
    if word[i] == word[i+1]:  # 이후 문자와 같은 문자라면 continue
      continue
    elif word[i] in word[i+1:]: # 만약 이후 문자와 다른 문자라면 이후에 지금(i번째) 문자와 같은 단어가 나오는지 확인( by "in" )
      count -= 1  # 같은 문자 등장시 그룹 단어 조건에 위배되므로 count에서 1 차감
      break

print(count)