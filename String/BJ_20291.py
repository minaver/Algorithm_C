# Topic : String _ 파일 정리
#
# Python 3 : 248 ms
import sys

N = int(input())

type_dict = dict()
for n in range(N):
  file = sys.stdin.readline().rstrip()

  file_type = file[file.find('.')+1:] # file에서 . index 이후에 있는 문자열만 따로 저장
  if file_type in type_dict:  # 딕셔너리에 해당 타입이 존재하면 +1
    type_dict[file_type] += 1
  else: # 딕셔너리에 해당 타입이 존재하지 않으면 1로 초기화
    type_dict[file_type] = 1

sorted_type = sorted(type_dict) # 사전순 정렬

for st in sorted_type:  # 사전순으로 정렬한 타입을(Key) 이용하여 딕셔너리에서 개수 가져옴(Value)
  print(st,type_dict[st],sep=" ")


