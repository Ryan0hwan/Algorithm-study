# 백준 11051. 이항계수2
https://www.acmicpc.net/problem/11051

# 1. top-down 방식(재귀. memoization 방식)

import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
cache = [[-1]*(i+1) for i in range(0, N+1)]
for k in range(N+1):
    cache[k][0] = 1
    cache[k][k] = 1

def f(n, k):
   if cache[n][k] == -1:       # 아직 진행이 안되었으면.
       cache[n][k] = f(n-1, k-1) + f(n-1, k)
   
   return cache[n][k]          # 값이 있다면

print(f(N, K)%10007)

'''
# 2. Bottom-up 방식(Tabulation 방식)

N, K = map(int, input().split())
cache = [[-1]*(i+1) for i in range(0, N+1)]
for k in range(N+1):
    cache[k][0] = 1
    cache[k][k] = 1

for n in range(N+1):
    for k in range(n):
        if cache[n][k] == -1:
            cache[n][k] = cache[n-1][k-1] + cache[n-1][k]


print(cache[N][K] %10007)
'''
