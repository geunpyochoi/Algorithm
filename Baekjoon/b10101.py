l = []
for _ in range(3):
  l.append(int(input()))
if l[0] == 60 and l[1] == 60 and l[2] == 60:
  print("Equilateral")
elif l[0]+l[1]+l[2] == 180 and (l[0] == l[1] or l[1] == l[2] or l[2] == l[0]):
  print("Isosceles")
elif l[0]+l[1]+l[2] == 180 :
  print("Scalene")
else:
  print("Error")