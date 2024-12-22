# 9012번. 올바른 괄호 쌓기.  
# 전형적인 STACK문제. 여는 괄호의 순서와 닫는 괄호의 순서가 역순. 

k = int(input())
for _ in range(k):
   for ch in input():
      stk = []
      isVPS = True
      
      if ch == '(':
         stk.append(ch)
      else:
         if stk:             # ')'을 없애버리는 걸로 표현한거지
            stk.pop()
         else:
            isVPS = False    # ')'이 더 많은 경우
            break
   if stk:                   # '('가 더 많은 경우.
      isVPS = False
   
   print('Yes' if isVPS else 'NO')
