s = input()
ans = []
for i in range(0,len(s)):
    ans.append(s[i:len(s)])
ans = sorted(ans)
for j in ans:
    print(j)
