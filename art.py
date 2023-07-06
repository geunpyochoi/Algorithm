t = int(input())

for _ in range(t):
  n = int(input())
  m = int(input())
  rec = list(map(int,input()))
  res = [] # res[i][0] 작품 번호 , res[i][1] 추천수, res[i][2] 들어온 순서
  if m <= n:
    for i in range(m):
      res.append(rec[i])
    for j in range(m):
      print(res[j],'',end='')
    print()
  for _ in range(n):
    res.append([0,0,0])
  for i in range(len(rec)):
    k = 0
    for j in range(1,len(res)):
      if res[k][1] > res[j][1]:
        k = j
      elif res[k][1] == res[j][1]:
        if res[k][2] > res[j][2]:
          k = j
      
  