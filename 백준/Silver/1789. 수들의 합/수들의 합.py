n = int(input())
sum = 0
ans = 0

for i in range(1,n+1):
  sum += i
  ans += 1
  if sum > n:
    ans -= 1
    break
  
print(ans)