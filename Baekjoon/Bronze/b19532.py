l = list(map(int,input().split()))
for i in range(-999,1000):
  for j in range(-999,1000):
    if (l[0]*i) + (l[1]*j) == l[2] and (l[3]*i) + (l[4]*j) == l[5]:
      print(i,j)