l = []
n = int(input())
for _ in range(n):
  a = list(map(int,input().split()))
  l.append(a)
sx,bx = 999999,-999999
sy,by = 999999,-999999
for i in range(n):
  if l[i][0] < sx:
    sx = l[i][0]
  if l[i][0] > bx:
    bx = l[i][0]
for i in range(n):
  if l[i][1] < sy:
    sy = l[i][1]
  if l[i][1] > by:
    by = l[i][1]
ans = (bx-sx) * (by-sy)
print(ans)     