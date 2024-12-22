# 11286번. heapq문제.  절대값이 가장 작은걸 출력하라.(같다면, 작은걸 출력)
# 문제에 N의 범위가 최대 100,000이네. 시간복잡도 위험.
# 튜플 비교를 이용!!. 
# (3,1) < (3,3)  앞의 값이 같으면 뒤에껄 비교하는 식이니. 앞에 절댓값을 두고, 뒤에 원값을

import heapq
import sys

input = sys.stdin.readline
hq = []
N = int(input())

for _ in range(N):
   k = int(input())
   if k != 0:
      heapq.heappush(hq, (abs(k), k))   # 튜플이용해서 절댓값 비교 표현
   else:                           # k가 0일때.
      if hq:                       # 힙큐에 무언가 있다면, 출력
         print(heapq.heappop(hq)[1])    # 원본값만 출력.
      else:                        # 힙큐에 아무것도 없다면, 0출력
         print(k)
         

# 음수는 절대값이 가장 작은 값을 뺀다는게 음수중에 가장 큰걸 뺀다는거지.
# 양수는 가장 작은걸 빼는거고.
# min_heap(양수)과 max_heap(음수)을 둘 다 만들어서 하는 방법이 있음
# 하지만 경우가 많아서 복잡함..  나중에 해봐.. 
