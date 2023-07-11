n,m = map(int,input().split())
l = []
ans = []
for _ in range(n):
  l.append(list(input()))
for i in range(0,n-7):
  for j in range(0,m-7):
    cnt = 0
    sample = l
    c,d = 0,0
    for p in range(i,i+8):
      for q in range(j,j+8):
        if p == i and q == j:
          continue
        elif q == j:
          if sample[p-1][q] == 'W':
            if sample[p][q] == 'W':
              cnt += 1
              sample[p][q] = 'B'
          elif sample[p-1][q] == 'B':
            if sample[p][q] == 'B':
              cnt += 1
              sample[p][q] = 'W'
        else:
          if sample[p][q-1] == 'W':
            if sample[p][q] == 'W':
              cnt += 1
              sample[p][q] = 'B'
          elif sample[p][q-1] == 'B':
            if sample[p][q] == 'B':
              cnt += 1
              sample[p][q] = 'W'
    ans.append(cnt)
print(ans)
print(len(ans))