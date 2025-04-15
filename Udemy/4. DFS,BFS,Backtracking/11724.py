# 백준 11724번.
# 그래프가 주어졌을 때, 연결요소를 구하라. 
# 간선의 최대 가능 크기가 매우크네 >> 인접행렬 사용이 유리함.
# 간단한 개수 구하는 문제는 dfs가 편함.
import sys

sys.setrecursionlimit(10**6)   # 파이썬에서는 재귀 제한이 1000인데, 이걸 늘려줄수있더라..  이거없으면 오류
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[0]*N for _ in range(N)]

# 입력값 채워주기
for _ in range(M):
    u, v = map(lambda x:x-1, map(int, input().split()))  # 람다이용해서 u,v가 1부터시작인걸 표시.  아니면, 위에 adj에 가로세로를 N+1로 하는것도 방법.
    adj[u][v] = adj[v][u] = 1    # 무방향(양방향)그래프이기 때문.

# 체크배열
chk = [False]*N            
ans = 0 

def dfs(now):
    for next in range(N):
      if adj[now][next] and not chk[next]:
        chk[next] = True
        dfs(next)
        

# 출력
for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)
