n = int(input())
l = list(map(int,input().split()))
m = int(input())
l2 = list(map(int,input().split()))
ans = [0 for _ in range(m)]
for i in range(m):
  for j in range(n):
    if l[j] == l2[i]:
      ans[i] = 1
      continue
for i in range(m):
  print(ans[i], end=' ')