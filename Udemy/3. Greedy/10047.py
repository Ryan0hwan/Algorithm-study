# 백준 11047번.
# Ai는 Ai-1의 배수  <<  문제를 보면 이 말이 적혀있다. 따라서 그리디로 풀 수 있는 것.

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]    # list comprehension으로 간편하게
coins.reverse()                             # 입력을 편하게 뒤집어주고. 
ans = 0

for coin in coins:
   ans += K//coin
   K %= coin

print(ans)
