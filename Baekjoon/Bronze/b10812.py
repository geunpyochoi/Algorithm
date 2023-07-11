n,m = map(int,input().split())
l = [k for k in range(n+1)]
for i in range(m):
  a,b,c = map(int,input().split())
  l1 = l[a:c]
  l2 = l[c:b+1]
  l3 = l2+l1
  l[a:b+1] = l3
for i in range(1,n+1):
  print(l[i],end=' ')