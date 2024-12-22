# 1302번. 가장많이팔린책을 출력하기.  딱봐도 map/dictionary 문제. 

d = dict()
N = int(input())

for _ in range(N):
   book = input()
   if book in d:               # 이미 있으면 value값 1 추가
      d[book] += 1
   else:                       # 없으면 value값 1로 만들기
      d[book] = 1
   
m = max(d.values())            # value가 가장 큰 값
candi = []                     # 답이 될 수 있는 후보들(value 값이 같은 것들)
for key, value in d.items():   # 표현 암기.
   if value == m:
      candi.append(key)

candi.sort()                   # value값이 같은 것들 중에 알파벳 순서가 가장 앞인 것.
print(candi[0])                # 한번에 print(sorted(candi)[0])을 해도 됨.

# 참고
# d.keys()    키들만 모아서 반환    
# d.values()  밸류들만 모아서 반환
# d.items()   키:밸류 형태로 모아서 반환
