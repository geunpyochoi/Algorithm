import sys

t = int(input())

for _ in range(0,t):
    n,c = map(int,sys.stdin.readline().split())
    l = [[0]*n for _ in range(n)]
    conv = []
    for p in range(0,c):
        a,b = map(int,sys.stdin.readline().split())
        l[a][b] = -1
        conv.append([])
        conv[p].append(a)
        conv[p].append(b)
        
    res = []
    val = 0
    for i in range(0,n):
        for j in range(0,n):
            if l[i][j] == -1:
                res.append(0)
                continue
            for k,p in conv:
                comp = abs(k - i) + abs(p - j)
                if comp <= 3:
                    val += 3
                elif comp <= 10:
                    val += 1
            res.append(val)
            val = 0
    num = max(res)
    idx = res.index(num)
    idx1 = int(idx/n)
    idx2 = idx%n
    print(idx1,idx2,num)
                  