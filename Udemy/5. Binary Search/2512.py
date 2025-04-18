# 백준 2512번.
# 문제의 변수 제한범위만 봐도 이분탐색으로 풀라는 문제.
# 사실상 이분탐색의 기본 구조.

N = int(input())
money = list(map(int, input().split()))
M = int(input())
money.sort()


low = 0; high = max(money)
mid = (low + high) // 2
ans = 0

def is_possible(mid):          # 배분한 예산의 총합이 국가예산을 초과하지 않는가 확인      
   return sum(min(m, mid) for m in money) <= M    # 이 함수에서 다른 알고리즘과 결합이 많이 되어 문제가 출제된다. 
                                                  # True/False가 나오는 알고리즘을 어떤식으로 만드느냐!! 
while low <= high:
    if is_possible(mid):       # 매개변수 탐색을 이용해서 마치 최적문제 -> 결정문제로 푸는
       low = mid + 1           # 가능하면 상한선 늘려주기
       ans = mid
    else:                      
       high = mid - 1          # 불가능하면 상한선 내리기
        
    mid = (low + high) // 2

print(ans)
