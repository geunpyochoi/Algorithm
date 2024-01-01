stick = [64,32,16,8,4,2,1]

x = int(input())
ans = 0
for i in stick:
  if x >= i:
    x -= i
    ans += 1
  if x == 0:
    break
print(ans)