import sys
t = int(sys.stdin.readline())

for i in range(0,t):
  n, m, d = map(int, sys.stdin.readline().split())
  l = []
  for j in range(0,m):
    a = input()
    arr = list(a)
    l.append(arr)
  d = (2*d) - 2
  n = (2*n) - 2
  m -= 1
  for _ in range(0,m):
    if 0 <= d + 1 <= n:
      if l[m][d+1] == '+':
        d += 2
        m -= 1
        continue
    if 0 <= d - 1 <= n:
      if l[m][d-1] == '+':
        d -= 2
        m -= 1
        continue
      m -= 1
  d = ((d+2)//2)
  print(d)