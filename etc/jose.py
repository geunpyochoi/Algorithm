t = int(input())

for _ in range(t):
  n,m = map(int,input().split())
  arr = [i for i in range(1,n+1)]
  res = []  
  num = 0  

  for t in range(n):
      num += m-1  
      if num >= len(arr):  
          num = num%len(arr)
  
      res.append(str(arr.pop(num)))
  print(res[-1])