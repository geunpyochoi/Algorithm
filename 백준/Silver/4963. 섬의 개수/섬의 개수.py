import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
  if x < 0 or x >= w or y < 0 or y >= h:
    return False
  if l[y][x] == 1:
    l[y][x] = 0
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    
    dfs(x+1,y+1)
    dfs(x-1,y+1)
    dfs(x-1,y-1)
    dfs(x+1,y-1)
    return True
  return False

while True:
  w,h = map(int,input().split())
  if w == 0 and h == 0:
    break
  l = []
  for i in range(h):
    l.append(list(map(int,input().split())))
  island = 0
  
  
  for i in range(h):
    for j in range(w):
      if dfs(j,i) == True:
        island += 1
  print(island)