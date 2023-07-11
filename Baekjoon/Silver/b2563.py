n = int(input())
l = []
x,y = 0,0
ans = 0
for i in range(n):
  a = list(map(int,input().split()))
  l.append(a)
ans = n*100
for i in range(n):
  for j in range(n):
    if i == j:
      continue
    else:
      if abs(l[i][0]-l[j][0])>0 and abs(l[i][1]-l[j][1])>0:
        x = abs(l[i][0]-l[j][0])
        y = abs(l[i][1]-l[j][1])
        ans -= ((10-x) * (10-y))/2
print(ans)

