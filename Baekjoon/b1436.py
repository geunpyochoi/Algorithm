n = int(input())
l = []
i = 666
while True:
  if len(l) == n:
    break
  else:
    if "666" in str(i):
      l.append(i)
  i += 1
print(l[n-1])