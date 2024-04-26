# dp 1463번
# backtracking해서 품.

N = int(input())

dp = [0]*(N+1)                 # 연산횟수를 저장하는 리스트 #초기값 설정
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0:               # 숫자가 2의 배수인 경우
       dp[i] = min(dp[i], dp[i//2] + 1)
    if i%3 == 0:               # 숫자가 3의 배수인 경우
       dp[i] = min(dp[i], dp[i//3] + 1)   
ans = dp[N]
print(ans)
