t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    box = []
    apple = []
    res = 0
    for _ in range(n):
        box.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                apple.append([i,j])
    while len(apple) != 0:
        tmp = []
        for i in apple:
            r = i[0]
            c = i[1]
            if r > 0 and box[r-1][c] == 0:
                box[r-1][c] = 1
                tmp.append([r-1,c])
            if c > 0 and box[r][c-1] == 0:
                box[r][c-1] = 1
                tmp.append([r,c-1])
            if r < n-1 and box[r+1][c] == 0:
                box[r+1][c] = 1
                tmp.append([r+1,c])
            if c < m-1 and box[r][c+1] == 0:
                box[r][c+1] = 1
                tmp.append([r,c+1])
        res += 1
        apple = tmp
    flag = 0
    res -= 1
    for i in range(n):
        if 0 in box[i]:
          flag = 1
          break
    if flag == 1:
        print(-1)
    else:
        print(res)
