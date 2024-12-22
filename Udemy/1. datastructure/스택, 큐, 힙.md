## 4. 스택 (C++에선 STL로 존재, 파이썬에선 리스트로 구현)
* LIFO
* 삽입, 삭제 : O(1)
* DFS와 관련

```
*  c++
stack<int> s;
s.push(123);
s.push(456);
s.push(789);
printf("size: %d\n", s.size());
while (!s.empty()) {
   printf("%d\n", s.top());
   s.pop();
}

*  python
s = []
s.append(123)
s.append(456)
s.append(789)
print("size:", len(s))
while len(s) > 0:
   printf(s[-1])
   s.pop(-1)
```
 
여기서 알아둬야 하는 것이 대부분의 pop()은 출력값 없이 빼는것만 하는것이다.

## 5. 큐 (C++, 파이썬 둘다 제공됨)

* FIFO
* 삽입, 삭제 : O(1)
* BFS와 관련

```
* C++
queue<int> q;
q.push(123);
q.push(456);
q.push(789);
printf("size: %d\n", q.size());
while(!q.empty()){
   printf("%d\n", q.front());    // front 주의
   q.pop();
}

* PYTHON
from collections import deque

q = deque()
q.append(123)       // appendleft(123)이건 왼쪽에서 넣는거야.
q.append(456)
q.append(789)
print("size:", len(q))
while len(q) > 0: 
   print(q.popleft())     // pop  반대로 이건 오른쪽에서 빼는거야
```

* C++에서는 front, rear 포인터 2개로 구현함.
* 파이썬에서는 collections에서 deque를 가져와서 씀.

(from queue import Queue도 가능하나, 이건 스레드세이프 기능 때문에 너무 느려)
deque는 앞에서도 넣고 빼고가 가능하고, 뒤에서도 넣고 빼고가 가능해


## 6. 우선순위 큐 (C++, 파이썬 둘다 제공됨.)

* 내부적으로 이진 트리 형태의 힙(Heap).
* 삽입, 삭제: O(log N)
* C++에서는 ROOT에 MAX값이, 파이썬에서는 ROOT에 MIN값이 위치한다.

```
* C++
priority_queue<int> pq;
pq.push(456);
pq.push(123);
pq.push(789);
printf("size: %d\n", pq.size());
while(!pq.empty()) {
   printf("%d\n", pq.top());
   pq.pop();                       // root에 위치한 max값이 빠짐.
}

* python
import heapq

pq = []
heqpq.heqppush(pq, 456)
heqpq.heqppush(pq, 123)
heqpq.heqppush(pq, 789)
print("size:", len(pq))
while len(pq) > 0:
   print(heapq.heappop(pq))          // root에 위치한 min값이 빠짐.
```

* 파이썬에는 from queue import PrioirityQueue도 있으나,,
* 마찬가지로 thread-safe 성격을 띠고 있어, 속도가 느리다.
* heapq 매번 쓰기 귀찮잖아.  import heapq as hq 써서  hq로 줄여쓰기 가능하다.
