n = int(input())

num = 1
for i in range(n,1,-1):
  num *= i
ans = 0
while True:
  if num % 10 == 0:
    num //= 10
    ans += 1
  else: break
print(ans)