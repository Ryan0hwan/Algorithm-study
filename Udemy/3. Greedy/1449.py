# 백준 1449번

N, L = map(int, input().split())
coord = [False]*1001                # 좌표를 일단 false로 채워진 리스트를 만듬.    # 만약 N의 제한범위가 엄청크면 그냥 구멍의 위치를 저장해서 다른로직으로 풀어야겠지.

for i in map(int, input().split()):  # 띄어쓰기 표현은 대개 이거.
   coord[i] = True                  # 이제 그게 있는곳만 True인거지.

ans = 0
x = 0
while x < 1001:
    if coord[x]:
       ans += 1
       x += L
    else:   
       x += 1

print(ans)
