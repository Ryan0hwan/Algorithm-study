import sys
s = []

num = int(sys.stdin.readline())
for i in range(num):
    sen = sys.stdin.readline().split()
    if sen[0] == 'top':
       if s: print(s[-1])
       else: print(-1)
    elif sen[0] == 'empty':
       if not s: print(1)
       else: print(0)
    elif sen[0] == 'size':
       print(len(s))
    elif sen[0] == 'pop':     
       if s: print(s.pop(-1))
       else: print(-1)

    elif sen[0] == 'push':
       s.append(sen[1])       
