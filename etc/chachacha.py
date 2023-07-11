import sys

t = int(input())

for _ in range(t):
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
  print(res)
  