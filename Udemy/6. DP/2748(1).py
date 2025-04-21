# 백준 2748. 피보나치수 2
# https://www.acmicpc.net/problem/2748

# 1. top-down 방식(재귀. memoization 방식)
"""def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        return f(n-2) + f(n-1)

print(f(int(input())))"""

## 아직 memoization을 적용하지 않은 상태. => 따라서 시간초과 발생.
## 코드 수정.

cache = [-1]*91     # memoization을 위해, dp테이블을 만들어둠.  음수값을 저장(구분위해)
cache[0] = 0
cache[1] = 1

def f(n):
   if cache[n] == -1:   # 아직 구하지 않은 값일 경우.
      cache[n] = f(n-2) + f(n-1)

   return cache[n]      # 이미 값이 있는 경우엔, 그냥 바로 사용.

print(f(int(input())))

# 둘이 시간 차이가 엄청나다. 
