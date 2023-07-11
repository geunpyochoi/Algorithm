n,m = map(int,input().split())
l = list(map(int,input().split()))
s,ans = 0,999999
left, right = 0, 0
while True:
  if s >= m:
    ans = min(ans,right-left)
    s -= l[left]
    left += 1
  elif left == n or right == n:
    break
  else:
    s += l[right]
    right += 1
if ans == 999999:
  ans = 0
print(ans)
