h = 0 #학점총합
p = 0 #평점총합     answer = p/h
for _ in range(20):
  a,b,c = map(str,input().split())
  if c == "P":
    continue
  b = float(b)
  h += b
  if c == "A+":
    p += 4.5 * b
  elif c == "A0":
    p += 4.0 * b
  elif c == "B+":
    p += 3.5 * b
  elif c == "B0":
    p += 3.0 * b
  elif c == "C+":
    p += 2.5 * b
  elif c == "C0":
    p += 2.0 * b
  elif c == "D+":
    p += 1.5 * b
  elif c == "D0":
    p += 1.0 * b
  elif c == "F":
    p += 0 * b
print(p/h)