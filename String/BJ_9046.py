# Topic : String _ 복호화
#
# Python 3 : 72ms
# 1. 문장속 등장하는 알파벳 횟수를 딕셔너리에 저장(def count)
# 2. 저장한 횟수 중 가장 많이 등장하는 알파벳(max_alp)과 그 등장 횟수(max)를 저장
# 3. 2에서 찾은 등장 횟수(max)와 동일한 등장 횟수를 갖는 알파벳이 존재하는지 확인하여 있다면 '?' 출력
# 4. 끝까지 결국 없다면 isMore이 False이므로 max_alp 출력

import sys

# 원하는 문장속에 들어있는 알파벳별 등장 횟수 구하는 함수
def count(line):
  alp = dict()

  for i in line:
    if i == ' ':  # 빈칸일 경우
      continue
    if i in alp:  # i가 이미 alp 안에 있을 경우
      alp[i] += 1
    else:         # i가 alp 안에 없을 경우
      alp[i] = 1
  
  return alp

N = int(sys.stdin.readline())

for i in range(N):
  T = sys.stdin.readline().rstrip()
  alp_count_dict = count(T)

  # 최대 등장 알파벳 확인
  max = 0
  for alp in alp_count_dict:
    if max < alp_count_dict[alp]:
      max = alp_count_dict[alp] # 등장 수 max
      max_alp = alp # 가장 많이 나온 알파벳 도출
  
  # 최대 등장 횟수가 동일한 알파벳이 있는지 확인
  isMore = False
  for alp in alp_count_dict:
    if max == alp_count_dict[alp] and alp != max_alp: # 최대 등장 횟수와 동일한 횟수를 가진 알파벳이 있는지 확인 and 위에서 찾은 알파벳이 아닌 알파벳 중
      print('?')
      isMore = True
      break
  
  if isMore == False:
    print(max_alp)