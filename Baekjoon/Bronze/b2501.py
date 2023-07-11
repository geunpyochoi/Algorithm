n, m = map(int,input().split())
cnt = 0
if n%m != 0 :
  print(0)
else:
  for i in range(1,n+1):
    if n%i == 0:
      cnt += 1
      if i == m:
        print(cnt)
        break