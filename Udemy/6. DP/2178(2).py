# 2. Bottom-up 방식(Tabulation 방식)
N = int(input())
cache = [-1]*91
cache[0] = 0
cache[1] = 1

for i in range(2, N+1):
   cache[i] = cache[i-2] + cache[i-1]

print(cache[N])

# 이 방식은 필요한 부분문제의 답만 알면 되는 memoization방식 과는 달리,
# 어떤 부분문제를 구해야 최종 문제로 갈 수 있을지에 대한 고민이 필요하다.
