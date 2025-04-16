# 백준 2178번.

from collections import deque

N, M = map(int, input().split())
adj = [[0]*M for _ in range(N)]


dy = (0,1,0,-1)
dx = (1,0,-1,0)

for i in range(N):
    adj[i] = list(map(int, input()))       # 입력에 공백이 없으니까.

def is_ok(y, x):                           # 범위체크
    return 0 <= y < N and 0 <= x < M

def bfs():
    chk = [[False]*M for _ in range(N)]
    q = deque()
    q.append((0,0,1))
    chk[0][0] = True

    while q:
        y, x, ans = q.popleft()           # ans를 큐에 같이 넣어서 계산하면 메모리를 아끼지.
        if y == N-1 and x == M-1:
            return ans

        for t in range(4):
            ny = y + dy[t]
            nx = x + dx[t]
            if is_ok(ny, nx) and not chk[ny][nx] and adj[ny][nx] == 1:
                chk[ny][nx] = True
                q.append((ny, nx, ans + 1))

    return -1                            # 도착점에 도달 못했을 경우.

print(bfs())
