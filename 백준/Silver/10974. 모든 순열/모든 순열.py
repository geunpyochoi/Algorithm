n = int(input())
arr = [i for i in range(1,n+1)]
t = []

def dfs(d):
  if d == n:
    print(*t)
    return 
  
  for i in range(n):
    if arr[i] not in t:
      t.append(arr[i])
      dfs(d+1)
      t.pop()

dfs(0)