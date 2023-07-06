n,m = map(int,input().split())
l1 = []
l2 = []
for i in range(n):
  l = list(map(int,input().split()))
  l1.append(l)
for i in range(n):
  li = list(map(int,input().split()))
  l2.append(li)
for i in range(n):
  for j in range(m):
    l1[i][j] += l2[i][j]
for i in range(n):
  for j in range(m):
    print(l1[i][j], end = ' ')
  print()