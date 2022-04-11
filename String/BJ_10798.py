# Topic : String _ 세로읽기
#
# Python 3 : 72ms

import sys

def readSero(list):
  max = 0
  for l in list:  # 입력으로 들어온 단어중 가장 긴 길이 구하기(max)
    if len(l) > max:
      max = len(l) 

  for i in range(max): # 각 글자의 세로 자리를 loop
    for word in list: # 5개의 단어를 loop   
      if len(word) > i: # 해당 단어의 길이가 i보다 큰 경우에만 print 아닐경우 그 단어는 그 세로 자리에 단어가 없는 것이다.
        print(word[i],end="")


word_list = list()
for i in range(5):
  word_list.append(sys.stdin.readline().rstrip())

readSero(word_list)