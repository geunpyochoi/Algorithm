while True:
  n = int(input())
  if n == -1 :
    break
  l = []
  for i in range(1,n):
    if n % i == 0:
      l.append(i)
  if sum(l) == n:
    print(n,"= ",end="")
    for i in range(len(l)):
      if i == len(l)-1:
        print(l[i])
      else:
        print(l[i],'+ ',end='')
  else:
    print(n,"is NOT perfect.")