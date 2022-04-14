# Topic : String _ 단어 정렬
#
# PyPy 3 : 173ms
# 
# list.sort() 함수가 길이도 sort 해준다는 사실은 처음알았다.
# 기존 작성했던 코드에 비해 1/10로 구현 시간이 줄었다.
# [ sort() 함수 정리 ]
# 1. 오름차순, 내림차순 : default or sort(reverse=False), sort(reverse=True)
# 2. key : sort 동작시 비교하기 전에 각 리스트 요소에 대해 호출할 함수(또는 다른 콜러블)를 지정하는 매개 변수가 key이다
# 예시 1)
# sorted("This is a test string from Andrew".split(), key=str.lower)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This'] 
# 
# 예시 2)
# student_tuples = [ ('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10) ]
# sorted(student_tuples, key=lambda student: student[2])   # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


import sys

N = int(sys.stdin.readline())
result = list()

for n in range(N):
  result.append(sys.stdin.readline().rstrip())

result = list(set(result))
result.sort()
result.sort(key = len)

for r in result:
  print(r)