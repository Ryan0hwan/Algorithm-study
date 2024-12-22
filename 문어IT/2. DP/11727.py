N = int(input())

# [1] dp[] table정의
# [2] dp[i]: 2*i 길이의 직사각형을 만드는 방법의 수
dp = [0]*(N+1)

# [3] dp[]의 초기값 설정
# n==1인 경우 dp[2]를 설정하면 index오류가 발생=>아래처럼 수정
# dp[1], dp[2] = 1, 3
dp[0], dp[1] = 1, 1

# [4] 범위정해서 반복처리
for i in range(2, N+1):
    dp[i]=dp[i-1]+dp[i-2]*2

ans = dp[N]
print(ans%10007)



# 그림을 그려서 규칙성을 찾음.  옆에 덧붙이는 방식
