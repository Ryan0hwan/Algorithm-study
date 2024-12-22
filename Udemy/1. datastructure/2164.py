# 2164번. 시뮬레이션 문제.  배열로 구현하면, 땡겨주는 것 때문에 시간복잡도 큼.
# 배열에서 삭제, 삽입을 구현하는 건 비효율적.  큐로 푸는게 효율적. 

from collections import deque

q = deque()
N = int(input())
for i in range(1, N+1):
   q.append(i)                     # 일단 큐에 다 넣어주고.
   
while len(q) > 1:
   q.popleft()
   q.append(q.popleft())
  
print(q.popleft())
