n = int(input())
for i in range(n):
  res = 0
  s = input()
  arr = list(s)
  for j in arr:
    if j == '(':
      res += 1
    elif j == ')':
      res -= 1
    if res < 0:
      print('NO')
      break
  if res > 0 :
    print('NO')
  elif res == 0:
    print('YES')