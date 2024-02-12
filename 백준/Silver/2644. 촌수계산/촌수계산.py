n = int(input())
a,b = map(int,input().split())
m = int(input())

family = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
  p1,p2 = map(int,input().split())
  family[p1].append(p2)
  family[p2].append(p1)

result = []
def dfs(v,chon):
  chon += 1
  visited[v] = 1
  if v == b:
    result.append(chon)
  for i in family[v]:
    if not visited[i]:
      dfs(i,chon)

dfs(a,0)

if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)