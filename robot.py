t = int(input())

for _ in range(t):
  n, d = map(int,input().split())
  r, c = map(int,input().split())
  arr = []
  for _ in range(n):
    arr.append(list(map(int,input().split())))
  # 동 1 , 서 3, 남 2, 북 0
  dir = [[-1,0],[0,1],[1,0],[0,-1]]
  res = 0
  while True:
    if arr[r][c] == 0:
      arr[r][c] = -1
      res += 1
    # row = r + dir[d][0]
    # col = c + dir[d][1]
    row = r + dir[(d+3)%4][0]
    col = c + dir[(d+3)%4][1]
    
    if arr[row][col] == 0:
      