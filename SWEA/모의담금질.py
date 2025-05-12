import random
import math

T = int(input())

def cost():
   return random.random()

for i in range(1,4):
   T, T_end, k = map(float, (input().split()))
   count = 0; cost_pre = float('inf')

   while T > T_end:
      cost_new = cost(); count += 1
      diff = cost_new - cost_pre
      if diff < 0 or math.exp(-diff/T) > random.random():
         cost_pre = cost_new
      T = T*k

   print(f'#{i} {count}')
