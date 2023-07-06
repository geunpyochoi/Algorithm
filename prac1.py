t = int(input())

for _ in range(t):
  # n,m = map(int,input().split())
  # s = input()
  # s2 = input()
  # res = 0
  
  # for i in range(m):
  #   if s2[i] == s[0]:
  #     tmp = s2[i:i+n]
  #     if s == tmp:
  #       res = 1
  #       break
  # print(res)
  
  # n, m = map(int,input().split())
  # a = list(map(int,input().split()))
  # res = []
  # cnt = 0
  
  # for _ in range(n):
  #   res.append([0,0,-1])
  # for i in range(m):
  #   flag = 0
  #   for j in range(n):
  #     if a[i] == res[j][0]:
  #       res[j][1] += 1
  #       flag = 1
  #       break
  #   if flag == 1:
  #     continue
  #   if cnt < n:
  #     for k in range(n):
  #       if res[k][0] == 0:
  #         res[k][0] = a[i]
  #         res[k][1], res[k][2] = 0,i
  #         cnt += 1
  #         break
  #     continue
  #   rec, order = 999,9999
  #   r_idx, o_idx = 0, 0
  #   cnt2 = 0
  #   for p in range(n):
  #     if rec > res[p][1]:
  #       rec = res[p][1]
  #       r_idx = p
  #   for q in range(n):
  #     if rec == res[q][1]:
  #       cnt2 += 1
  #   if cnt2 > 1:
  #     for u in range(n):
  #       if order > res[u][2]:
  #         order = res[u][2]
  #         o_idx = u
  #     res[o_idx][0] = a[i]
  #     res[o_idx][1], res[o_idx][2] = 0 ,i
  #   else:
  #     res[r_idx][0] = a[i]
  #     res[r_idx][1], res[r_idx][2] = 0 ,i
  # res.sort()
  # for i in range(n):
  #   print(res[i][0],'',end='')
  # print()
  
  # n, d = map(int,input().split())
  # r, c= map(int,input().split())
  # a = []
  # for _ in range(n):
  #   a.append(list(map(int,input().split())))
  # dir = [[-1,0],[0,1],[1,0],[0,-1]]
  # res,flag,cnt = 0,0,0
  # while True:
  #   if a[r][c] == 0:
  #     a[r][c] = -1
  #     res += 1
  #     cnt = 0
  #   while True:
  #     if cnt == 4:
  #       d = (d+2) % 4
  #       nr = r + dir[d][0]
  #       nc = c + dir[d][1]
        
  #       if a[nr][nc] == 1:
  #         flag = 1
  #         break
  #       else:
  #         r = nr
  #         c = nc
  #         cnt = 0
  #         d = (d+2) % 4
  #       break
  #     nr = r + dir[(d+3)%4][0]
  #     nc = c + dir[(d+3)%4][1]
      
  #     if a[nr][nc] == 0:
  #       r = nr
  #       c = nc
  #       d = (d+3) % 4
  #       cnt = 0
  #       break
  #     else:
  #       d = (d+3) % 4
  #       cnt += 1
  #   if flag == 1:
  #     break
  # print(res)
  
  n,m = map(int,input().split())
  box = []
  apple = []
  res = 0
  for _ in range(n):
    box.append(list(map(int,input().split())))
  for i in range(n):
    for j in range(m):
      if box[i][j] == 1:
        apple.append([i,j])
  while len(apple) != 0:
    tmp = []
    for i in apple:
      r = i[0]
      c = i[1]
      
      if r > 0 and box[r-1][c] == 0:
        box[r-1][c] = 1
        tmp.append([r-1,c])
      if c > 0 and box[r][c-1] == 0:
        box[r][c-1] = 1
        tmp.append([r,c-1])
      if r < n-1 and box[r+1][c] == 0:
        box[r+1][c] = 1
        tmp.append([r+1,c])
      if c < m-1 and box[r][c+1] == 0:
        box[r][c+1] = 1
        tmp.append([r,c+1])
    res += 1
    apple = tmp
  res -= 1
  flag = 0
  for i in range(n):
    if 0 in box[i]:
      flag = 1
      break
  if flag == 1:
    print(-1)
  else:
    print(res)