t = int(input())

for _ in range(t):
  n, m = map(int,input().split())
  s1 = input()
  s2 = input()
  if s1 in s2 :
    print(1)
  else :
    print(0)