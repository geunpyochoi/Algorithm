s = input()
l,r = 0, len(s)-1
ans = 1
while l < r:
  if s[l] == s[r]:
    l += 1
    r -= 1
  else:
    ans = 0
    break
print(ans)