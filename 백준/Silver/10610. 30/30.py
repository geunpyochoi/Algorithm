n = input()

if '0' not in n:
  print(-1)
else:
  num = 0
  for i in n:
    num += int(i)
  if num % 3 != 0:
    print(-1)
  else:
    answer = sorted(n,reverse=True)
    answer = "".join(answer)
    print(answer)