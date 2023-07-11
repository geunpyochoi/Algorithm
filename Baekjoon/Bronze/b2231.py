n = int(input())
ans = 0
for i in range(0,n):
  s = 0
  for j in range(len(str(i))):
    a = str(i)
    s += int(a[j])
  if (s + i) == n:
    ans = i
    break
print(ans)