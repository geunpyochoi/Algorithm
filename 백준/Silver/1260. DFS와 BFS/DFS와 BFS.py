from collections import deque

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
for i in graph:
  i.sort()

def dfs(num):
  visited_dfs[num] = 1
  print(num,end=' ')
  for i in graph[num]:
    if not visited_dfs[i]:
      dfs(i)

def bfs(num):
  q = deque()
  q.append(num)
  visited_bfs[num] = 1
  while q:
    num = q.popleft()
    print(num,end=' ')
    for i in graph[num]:
      if not visited_bfs[i]:
        q.append(i)
        visited_bfs[i] = 1
    
dfs(v)
print()
bfs(v)