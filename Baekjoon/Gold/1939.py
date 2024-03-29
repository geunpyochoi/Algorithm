from collections import deque

def bfs(k):
    queue = deque([start_node])
    visited = [False] * (n+1)
    visited[start_node] = True
    while queue:
        x = queue.popleft()
        for y, weight in a_list[x]:
            if not visited[y] and weight >= k:
                visited[y] = True
                queue.append(y)
    return visited[end_node]

t = int(input())
for _ in range(0,t):
  n, m, start_node, end_node = map(int, input().split())

  a_list = [[] for _ in range(n+1)]
  start = 1000000000
  end = 1
  for _ in range(m): 
    a, b, c = map(int, input().split())
    a_list[a].append((b, c))
    a_list[b].append((a, c))
    start = min(start, c)
    end = max(end, c)


  res = start
  while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        res = mid
        start = mid + 1
    else:
        end = mid - 1

  print(res)
