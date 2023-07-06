from pydoc import visiblename
import sys
"""def ladder(l,n,m,d):
  for _ in range(m):
    if l[m][d] == '?':
      break
    if 0 <= d+1 and d+1 <= n:
      if l[m][d+1] == '+':
        d += 2
        m -= 1
        continue
    if 0 <= d-1 and d-1 <= n:
      if l[m][d-1] == '+':
        d -= 2
        m -= 1
        continue
    m -= 1
  return m,d"""
  
  
t = int(input())

for _ in range(t):
  """계산기
  n = int(input())
    l = input().split()
    num = []
    stack = []
    prior = {'*':3,'+':2,'-':2,'(':1}
    for i in range(0,len(l)):
        if l[i].isdigit():
          num.append(l[i])
        elif l[i] == '(':
            stack.append(l[i])
        elif l[i] == ')':
            while stack[-1] != '(':
                num.append(stack.pop())
            stack.pop() 
        else: 
            while stack and prior[l[i]] <= prior[stack[-1]]:
                num.append(stack.pop()) 
            stack.append(l[i])
    while len(stack) != 0:
        num.append(stack.pop())
    n1 = 0
    n2 = 0
    b = len(num)
    for j in range(0,b):
        if num[j].isdigit():
            stack.append(int(num[j]))
        elif num[j] == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1+n2)
        elif num[j] == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
        elif num[j] == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1*n2)
    print(stack[0])"""
  """동적배열
  n = int(input())
    arr = [[0]*2 for _ in range(101)]
    cnt = 0
    # 데이터 수, 크기
    for _ in range(n):
        a, c = map(int,sys.stdin.readline().split())
        arr_size = 2
        if arr[a][1] == 0:
            while arr_size <= c:
                arr_size *= 2
            arr[a][0] += c
            arr[a][1] = arr_size        
        elif arr[a][1] < arr[a][0] + c:
            cnt += arr[a][0]
            arr[a][0] += c
            while True:
                if arr[a][1] <= arr[a][0]:
                    arr[a][1] *= 2
                else:
                    break
        else:
            arr[a][0] += c
    print(cnt)"""
  """ 택배배송
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
"""
  """" 차차차
  n = int(input())
  arr = [[0]*5 for _ in range(n+1)]
  dp = [[0]*5 for _ in range(n+1)]
  for i in range(0,5):
    if i == 2:
      continue
    else:
      dp[0][i] = -1
  for _ in range(n):
    a = map(int,input().split())
    l = list(a)
    arr.append(l)
  arr.reverse()
  arr.insert(0,[0,0,0,0,0])
  for i in range(1,n+1):
    for j in range(0,5):
      if arr[i][j] == 1:
        dp[i][j] = -1
        continue
      dp[i][j] = dp[i-1][j]
      if j>0:
         dp[i][j] = max(dp[i-1][j-1], dp[i][j])
      if j<4:
         dp[i][j] = max(dp[i-1][j+1], dp[i][j])

      if arr[i][j]>1:
         dp[i][j] += arr[i][j]
      if j>0 and arr[i][j-1] == 1:
         dp[i][j] += 1
      if j<4 and arr[i][j+1] == 1:
        dp[i][j] += 1
  res = 0
  for i in range(0,5):
    res = max(dp[n][i],res)
  print(res)""""
  """ 미로탐색
  n,m = map(input().split())
  miro = []
  queue = [(0,0)]
  visited = [[0]*m for _ in range(n)]
  visited[0][0] = 1
  for _ in range(n):
    a = input()
    miro.append(list(a))
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  while queue:
    x,y = queue.pop(0)
    if x == n - 1 and y == m - 1:
      print(visited[x][y])
      break
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if visited[nx][ny] == 0 and miro[nx][ny] == '1':
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx,ny)) """
            
  """ 치유와드
  n, m = map(int, input().split())
  arr = [[0]*n for _ in range(n)]
  a, b = map(int, input().split())
  for _ in range(a):
    r,c = map(int,input().split())
    for i in range(0,n):
      for j in range(0,n):
        if max(abs(i-r),abs(c-j)) - m - 1 < 0:
          arr[i][j] += max(abs(i-r),abs(c-j)) - m - 1
    arr[r][c] += 1
  for _ in range(b):
    r,c = map(int,input().split())
    for i in range(0,n):
      for j in range(0,n):
        if (m+1) - (abs(i-r) + abs(j-c))  > 0:
          arr[i][j] += (m+1) - (abs(i-r) + abs(j-c))
    arr[r][c] -= 1
  for i in range(0,n):
    for j in range(0,n):
      print(arr[i][j], end='')
    print("")"""
  """사다리2
  n,m,d = map(int,input().split())
  l = []
  for _ in range(m):
    a = input()
    l.append(list(a))
  d = (d*2) - 2
  n = (n*2) - 2
  m -= 1
  m,d = ladder(l,n,m,d)
  cnt = 0
  res = []
  if d == 0 or d == n:
    flag = 2
  else :
    flag = 3
  while cnt != flag :
    k = m
    p = d
    if flag == 2:
      if p == n:
        if cnt == 0:
          k -= 1
          k,p = ladder(l,n,k,p)
          res.append((p+2)//2)
          cnt += 1
          continue
        elif cnt == 1:
          k -= 1
          p -= 2
          k,p = ladder(l,n,k,p)
          res.append((p+2)//2)
          cnt += 1
          continue
      if p == 0:
        if cnt == 0:
          k -= 1
          k,p = ladder(l,n,k,p)
          res.append((p+2)//2)
          cnt += 1
          continue
        elif cnt == 1:
          k -= 1
          p += 2
          k,p = ladder(l,n,k,p)
          res.append((p+2)//2)
          cnt += 1
          continue
    if flag == 3:
      if cnt == 0:
          k -= 1
          k,p = ladder(l,n,k,p)
          res.append((p+2)//2)
          cnt += 1
          continue
      elif cnt == 1:
          k -= 1
          p -= 2
          k,p = ladder(l,n,k,p)
          res.append((p+2)//2)
          cnt += 1
          continue
      elif cnt == 2:
          k -= 1
          p += 2
          k,p = ladder(l,n,k,p)
          res.append((p+2)//2)
          cnt += 1
          continue
  res.sort()
  print(res)"""
  """편세권
  n, c = map(int, input().split())
  m = [[0]*n for _ in range(n)]
  conv = []
  res = []
  for _ in range(c):
    r,c = map(int,input().split())
    m[r][c] = -1
    conv.append([r,c])
  val = 0
  for i in range(0,n):
    for j in range(0,n):
      if m[i][j] == -1 :
        res.append(0)
        continue
      else:
        for k,p in conv:
          comp = abs(k-i) + abs(p-j)
          if comp <= 3:
            val += 3
          elif comp <= 10:
            val += 1
        res.append(val)
        val = 0
  num = max(res)
  idx1 = int(res.index(num)/n)
  idx2 = res.index(num)%n

  print(idx1,idx2,num)"""
  """ 사다리타기
  n,m,d = map(int,input().split())
  l = []
  for _ in range(m):
    a = input()
    l.append(list(a))
  n = (2*n) - 2
  d = (2*d) - 2
  m -= 1
  for i in range(m):
    if 0 <= d + 1 and d + 1<= n:
      if l[m][d+1] == '+':
        d += 2
        m -= 1
    elif 0 <= d - 1 and d - 1 <= n:
      if l[m][d-1] == '+':
        d -= 2
        m -= 1
    m -= 1
  print((d//2)+2)"""
  """ 주식투자
  d = int(input())
  arr = list(map(int,input().split()))
  arr.reverse()
  b = 0
  res = 0
  for i in range(0,d):
    if b < arr[i]:
      b = arr[i]
    else:
      res += b - arr[i]
  print(res)"""
  