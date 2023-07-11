a,b = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
diff = 0
for i in range(a):
  for j in range(a):
    for k in range(a):
      if i == j or j == k or i == k:
        continue
      else:
        if l[i] + l[j] + l[k] > b:
          continue
        elif l[i] + l[j] + l[k] == b:
          diff = b
          break
        else:
          if b - (l[i] + l[j] + l[k]) < b - diff:
            diff = l[i] + l[j] + l[k]
print(diff)