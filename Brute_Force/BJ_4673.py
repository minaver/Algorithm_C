# Topic : Brute_Force  _ 셀프 넘버
#
# PyPy 3 : 76ms
# set 차집합 연산 사용

# set로 한 이유는 list로 구현했을때 all_num에서 non_self_num을 빼는건 어렵다
# 차집합 연산을 사용하기 위해 set을 사용
all_num = set(range(1,10000)) # 1~9999까지의 모든 수 저장
non_self_num = set()  # self num가 아닌 수 저장할 곳

for num in range(1,9993):
  num += sum(map(int,str(num))) # num을 str화 한후 각각을 다시 int로 바꿔 sum해준다. 이를 num에 더한다.
  if num < 10000: # 10000이하일 경우만 n_s_n에 저장
    non_self_num.add(num)

result = sorted(all_num - non_self_num) # 차집한 연산후 순서대로 출력하기 위해 sorted 해준다.

for r in result:
  print(r)
    


