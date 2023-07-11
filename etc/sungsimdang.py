t = int(input())

for _ in range(t):
  n,m = map(int,input().split())
  a = []
  for _ in range(n):
    p = input().split()
    a.append(list(p))
  print(a)
  