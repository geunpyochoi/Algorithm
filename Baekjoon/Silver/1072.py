import math
a,b = input().split()
a = int(a)
b = int(b)

z = int(b* 100/a)
res = 0
start = 0
end = 1000000000
if z >= 99:
  res = -1
else:
  while start <= end:
    mid = (start + end)//2
    if int(((b + mid) * 100/( a + mid))) > z:
      res = mid
      end = mid - 1
      
    else:
      start = mid + 1
print(res)
