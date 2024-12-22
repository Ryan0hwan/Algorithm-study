# 2309번.  9명 난쟁이 중에, 진짜 7명 난쟁이를 찾는 문제. 7명 난쟁이의 키의 합은 100.  답을 오름차순으로 출력.

from itertools import combinations

arr = []
for _ in range(9):
   k = int(input())
   arr.append(k)                   # 이 4줄을 한 줄에 표현하는게.  arr = [int(input()) for _ in range(9)]
   
for i in combinations(arr, 7):
    if sum(i) == 100:              # 7개짜리 조합 중에 합이 100이라면, 
        for height in sorted(i):   # 합이 100인 i조합 안에서 정렬된 순서대로 하나씩 한줄에 출력하기.
           print(height)
        break                      # 답이 여러개일수 있으니..
