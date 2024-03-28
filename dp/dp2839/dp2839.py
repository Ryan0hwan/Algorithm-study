# [실버4] 설탕배달
# https://www.acmicpc.net/problem/2839

M = int(input())
cnt = 0

while True:
    if M % 5 == 0:  # M이 5의 배수인 경우
        cnt += M // 5
        print(cnt)
        break
    elif M < 0:  # M이 음수가 되면 봉지로 만들 수 없는 경우
        print(-1)
        break
    else:  # 5의 배수가 아닌 경우 3을 빼야 함
        M -= 3
        cnt += 1
      
