n = int(input())

val = 0
for i in range(1, n+1):
    arr = list(map(int, str(i)))
    if i < 100:
        val += 1 
    elif arr[0]-arr[1] == arr[1]-arr[2]:
        val += 1 
print(val)