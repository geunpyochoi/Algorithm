l = []
n = int(input())
for _ in range(n):
  m = int(input())
  l.append(m)
for i in range(n):
  q,d,n,p = 0,0,0,0
  if l[i] >= 25:
    q = l[i] // 25
    l[i] %= 25
  if l[i] >= 10:
    d = l[i] // 10
    l[i] %= 10
  if l[i] >= 5:
    n = l[i] // 5
    l[i] %= 5
  if l[i] > 0:
    p = l[i]
  print(q,d,n,p) 
