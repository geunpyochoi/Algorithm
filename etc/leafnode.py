def dfs(node):
  a[node] = -2
  for i in range(n):
    if node == a[i]:
      dfs(i)      

t = int(input())

for _ in range(t):
  n,m = map(int,input().split())
  a = list(map(int,input().split()))
  res = 0
  dfs(m)
  for i in range(n):
    if a[i] != -2 and i not in a:
      res += 1
  print(res)
  
      
  