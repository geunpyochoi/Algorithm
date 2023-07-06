l = []
for i in range(9):
  a = list(map(int,input().split()))
  l.append(a)
m = -1
r,c = 0,0
for i in range(9):
  for j in range(9):
    if l[i][j] > m:
      m = l[i][j]
      r,c = i,j
print(m)
print(r+1,c+1)