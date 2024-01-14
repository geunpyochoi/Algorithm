s = input()

for i in range(0,len(s)):
  if(i != 0 and i % 10 == 0):
    print()
  print(s[i],end='')