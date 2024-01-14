n = input()

cnt = 0
for i in range(1,len(n)):
  if n[i-1] != n[i]:
    cnt += 1
print((cnt+1)//2)