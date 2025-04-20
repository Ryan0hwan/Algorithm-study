# 백준 10815번.

from bisect import bisect_left, bisect_right

N = int(input())
cards = list(map(int, input().split()))
cards.sort()

M = int(input())
qry = list(map(int, input().split()))

# 이걸 선형탐색으로 풀면 시간복잡도가 O(N*M)인데, 제한범위 고려하면 엄청 크다.
# 이걸 이분탐색으로 풀면 시간복잡도가 O(logN*M)이기에 훨씬 빠름 [정렬은 그 전에 하는거고]

ans = []

for q in qry:
    l = bisect_left(cards, q)
    r = bisect_right(cards, q)
    ans.append(1 if r-l else 0)
   
print(*ans)
