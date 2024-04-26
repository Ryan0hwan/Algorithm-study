## 기본설정
손으로 그려보면서 이해부터 하는게 우선. 
ans_bfs or ans_dfs : 그래프를 adjacency matrix로 나타냄. / 양방향, 단방향 여부 확인. 
v[] :방문표시하는 배열. 
ans : 정답표시할 배열

## DFS 풀이법
dfs(c)
1. v[c] = 1, ans_dfs.append(c)
2. for n in adj[c]
        if not v[n]: dfs(n)

## BFS 풀이법
bfs(s)
1. q(큐), v(방문 표시), 변수 생성
2. q에 초기 데이터(들) 삽입, v[]표시, ans처리   << 단위작업
3. while q:
     q에서 데이터 한개 꺼냄.
     for 4방향, 8방향... 조건 맞으면 q에 삽입.

     문제가 바뀌면, 마지막 줄의 조건이 바뀌는 것이고, 대강 비슷함 
