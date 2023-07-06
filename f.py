t = int(input())

for _ in range(t):
  n,m = map(int,input().split())
  dir = [[-1,0],[1,0],[0,-1],[0,1]]
  box = []
  arr = [[999]*m for _ in range(n)]
  apple = []
  res = 0
  cnt = 0
  for _ in range(n):
    box.append(list(map(int,input().split())))
  for i in range(n):
    for j in range(m):
      if box[i][j] == 1:
          apple.append([i,j])
      elif box[i][j] == 0:
                cnt += 1
  if cnt == 0:
    print(res)
    continue
  while len(apple) > 0 and cnt > 0:
    r = apple[0][0]
    c = apple[0][1]
    apple.pop(0)
    for i in range(4):
      row = dir[i][0] + r
      col = dir[i][1] + c
      if 0 <= row < n and 0 <= col < m:
        if box[row][col] == 0 and arr[row][col] == 999:
          arr[row][col] = min(arr[row][col], arr[r][c]+1)
          res = max(res,arr[row][col])
          apple.append([row,col])
          cnt -= 1
  flag = 0
  for i in range(n):
      for j in range(m):
          if box[i][j] == 0:
              flag = 1
              break
      if flag == 1:
          break
  if flag == 1:
      print(-1)
  else:
      print(res)