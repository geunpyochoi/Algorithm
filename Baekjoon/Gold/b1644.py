n = int(input())
l,r = 0,0
s = 0
p = []
ans = 0
for i in range(2,n+1):
  cnt = 0
  for j in range(1,i):
    if i % j == 0:
      cnt += 1
    if cnt > 1:
      break
  if cnt == 1:
    p.append(i)
while True:
  if s == n:
    ans += 1
    
    l += 1
    s = 0
  elif s > n:
    s -= p[l]
    l += 1
  else:
    if r > len(p)-1 or l > r:
      break
    else:
      s += p[r]
      r += 1
print(ans)