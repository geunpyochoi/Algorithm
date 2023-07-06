from sys import stdin
from collections import deque
t = int(stdin.readline())
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]
for _ in range(t):
  n = int(input())
  
  climb = []
  for _ in range(n):
    climb.append(list(stdin.readline().split()))
  
  res = [[0]*n for _ in range(n)]
  res[n-1][0] = 1
  hold = deque()
  hold.append((n-1,0))
  
  while len(hold) != 0:
    r = hold[0][0]
    c = hold[0][1]
    
    h = res[r][c]
    hold.popleft()
    
    for i in range(4):
      nx = r + dx[i]
      ny = c + dy[i]
      if 0 <= nx < n and 0 <= ny < n and climb[nx][ny] == "H":
        if res[nx][ny] == 0 or res[nx][ny] > res[r][c]+1:
          res[nx][ny] = res[r][c]+1
          hold.append([nx,ny])
    if c-2 >= 0 and r > 0 and climb[r][c-2] == 'H' and climb[r][c-1] == '.' and climb[r-1][c] == '.' and climb[r-1][c-1] == '.' and climb[r-1][c-2] == '.' and res[r][c-2] == 0:
      res[r][c-2] = h + 1
      hold.append([r,c-2])
    if c+2 <= n-1 and r > 0 and climb[r][c+2] == 'H' and climb[r][c+1] == '.' and climb[r-1][c] == '.' and climb[r-1][c+1] == '.' and climb[r-1][c+2] == '.' and res[r][c+2] == 0:
      res[r][c+2] = h + 1
      hold.append([r,c+2])
    if c-3 >= 0 and r > 0 and climb[r][c-3] == 'H' and climb[r][c-1] == '.' and climb[r][c-2] == '.' and climb[r-1][c] == '.' and climb[r-1][c-1] == '.' and climb[r-1][c-2] == '.' and climb[r-1][c-3] == '.' and res[r][c-3]==0:
      res[r][c-3] = h + 1;
      hold.append([r, c-3]);
    if c+3 <= n-1 and r > 0 and climb[r][c+3] == 'H' and climb[r][c+1] == '.' and climb[r][c+2] == '.' and climb[r-1][c] == '.' and climb[r-1][c+1] == '.' and climb[r-1][c+2] == '.' and climb[r-1][c+3] == '.' and res[r][c+3]==0:
      res[r][c+3] = h + 1
      hold.append([r, c+3])
    # 3번
    if r >= 2 and climb[r-1][c] == '.' and climb[r-2][c] == 'H' and res[r-2][c] == 0:
      res[r-2][c] = h + 1
      hold.append([r-2,c])
    # 4번
    if r >= 1 and c >= 1 and climb[r-1][c] == '.' and climb[r][c-1] == '.' and climb[r-1][c-1] == 'H' and res[r-1][c-1] == 0 :
      res[r-1][c-1] = h + 1
      hold.append([r-1,c-1])
    # 5번
    if r >= 1 and c < n - 1 and climb[r][c+1] == '.' and climb[r-1][c] == '.' and climb[r-1][c+1] == 'H' and res[r-1][c+1] == 0 :
      res[r-1][c+1] = h + 1
      hold.append([r-1,c+1])
  for i in range(n):
    for j in range(n):
      if res[i][j] == 0 and climb[i][j] == 'H':
        res[i][j] = -1
  for i in range(n):
    for j in range(n):
      print(res[i][j],'',end='')
    print()
  
  