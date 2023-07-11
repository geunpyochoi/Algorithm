n = int(input())
l = list(map(int,input().split()))
l.sort()
left, right = 0,n-1
std = 0
a = -1000000999
ans = [0,0]
while left < right:
  avg = (l[left]+l[right])/2
  if  abs(std-a) > abs(std-avg):
    a = avg
    ans[0],ans[1] = l[left], l[right]
  if avg < 0 :
    left += 1
  else:
    right -= 1
for i in range(2):
  print(ans[i], end=' ')