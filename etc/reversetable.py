t = int(input())

for _ in range(t):
  n = list(map(int,input().split()))
  res = []
  for i in range(n[0],0,-1):
    res.insert(n[i],i)
  for j in range(n[0]):
    print(res[j],'',end='')
  print()
  