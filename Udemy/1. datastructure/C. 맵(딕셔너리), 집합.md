## 7. 맵(c++), 딕셔너리 (python)

* KEY-VALUE 쌍.  JSON 형태
* KEY끼리는 중복을 허용하지 않는다.

```
// C++
map<string, int> m;
m["Yoondy"] = 40;                윤디가 키, 40이 밸류
m["Sky"] = 100;
m["Jerry"] = 50;
printf("size: %d\n", m.size());
for (auto p: m)
   printf("%d, %d\n", p.first, p.second);
```

* C++의 MAP에서의 삽입, 삭제 : O(log N)

```
// PYTHON
m = {}
m["Yoondy"] = 40
m["Sky"] = 100
m["Jerry"] = 50
print("size:", len(m))
for k in m:
   print(k, m[k])
```

* python의 MAP에서의 삽입, 삭제 : O(1)
* 코드상으로는 사용법에 차이가 없어보이나, 하지만 둘은 구현에서 차이가 난다.
* C++은 RED-BLACK 트리 / PYTHON은 HASH로 구현

## 8. 집합 (맵, 딕셔너리랑 비슷)

* 중복 X
* 마찬가지로 c++에선 red-black트리로, python에선 hash로.  그래서 시간복잡도 같음.
* 집합에서 pop()을 쓰면, 랜덤하게 빠지는거라, 뭐가 빠질지 알 수 없다.
* 그래서 remove(k)를 쓰면, 특정값을 뺄 수 있다.

```
// C++
set<int> s;
s.insert(456);
s.insert(12);
s.insert(456);
s.insert(7890);
s.insert(7890);
s.insert(456);
printf("size: %d\n", s.size());
for (auto i:s)
   printf("%d\n", i);
```

* C++의 집합에서의 삽입, 삭제 : O(log N)

```python
// python
s = set()
s.add(456)
s.add(12)
s.add(456)                 // 중복값이라고 오류는 안나는데 무시하는거지
s.add(7890)
s.add(7890)
s.add(456)
print("size:", len(s))         // 3개만 나옴
for i in s:
   print(i)
```

* python의 집합에서의 삽입, 삭제 : O(1)
