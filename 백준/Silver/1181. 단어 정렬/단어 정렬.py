n = int(input())
data = []
for _ in range(n) :
    value = input()
    data.append(value)

data = list(set(data))
data = sorted(data, key=lambda x: (len(x), x))

for d in data :
    print(d)