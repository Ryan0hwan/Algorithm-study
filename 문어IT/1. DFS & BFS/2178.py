# 2차원이 나오네   https://www.acmicpc.net/problem/2178

# 함수 
def bfs(si, sj, ei, ej):    # 시작좌표와 끝좌
  q = []
  v = [[0]*M for _ in range(N)]

  q.append((si,sj))      # q에 초기데이터 삽입 후, v에 방문표시 
  v[si][sj] = 1

  while q:
    ci, cj = q.pop(0)
    if (ci, cj) == (ei, ej):                                            # return값 처리. 
      return v[ei][ej]
      
    for di,dj in ((-1,0), (1,0), (0,-1), (0,1)):                        # 4방향
       ni, nj = ci+di, cj+dj                                            # 현재위치에서 4방향 고려
       if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and v[ni][nj] == 0:  # 범위벗어나지 않으면서, arr가 1이면서, 방문하지 않았다면, 
          q.append((ni, nj))
          v[ni][nj] = v[ci][cj] + 1    # 현재거리에다가 1더해 
           
# 입력
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

# 출력
ans = bfs(0, 0, N-1, M-1)  
print(ans)
  
