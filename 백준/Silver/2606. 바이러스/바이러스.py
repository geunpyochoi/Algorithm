n = int(input()) # 컴퓨터 대수
m = int(input()) # 연결 컴퓨터 쌍의 수

pc = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  pc[a].append(b)
  pc[b].append(a)
def dfs(num):
  for j in range(len(pc[num])):
    if visited[pc[num][j]] == 1:
      continue
    else:
      visited[pc[num][j]] = 1
      dfs(pc[num][j])
dfs(1)
if sum(visited) == 0:
  print(0)
else:
  print(sum(visited)-1)