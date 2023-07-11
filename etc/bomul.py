import sys

t = int(input())
for _ in range(t):
    n = int(input())
    m = []
    for _ in range(n):
        a = list(input().split())
        m.append(a)
    pre = "B"
    res = [['-']*n for _ in range(n)]
    now = m[0][0][0]
    i,j = 0,0
    while True: 
        now = m[i][j][0]
        if pre == "F":
            if now == "F":
                pre = "F"
                if 'F' in res[i][j]:
                    break
                res[i][j] += 'F'
                i += int(m[i][j][1])
            elif now == "R":
                pre = "R"
                if 'R' in res[i][j]:
                    break
                res[i][j] += 'R'
                j += int(m[i][j][1])
            elif now == "L":
                pre = "L"
                if 'l' in res[i][j]:
                    break
                res[i][j] += "L"
                j -= int(m[i][j][1])
            elif now == "B":
                pre = "B"
                if 'B' in res[i][j]:
                    break
                res[i][j] += 'B'
                i -= int(m[i][j][1])
            continue
        if pre == "R":
            if now == "F":
                pre = "R"
                if 'R' in res[i][j]:
                    break
                res[i][j] += 'R'
                j += int(m[i][j][1])
            elif now == "R":
                pre = "B"
                if 'B' in res[i][j]:
                    break
                res[i][j] += 'B'
                i -= int(m[i][j][1])
            elif now == "L":
                pre = "F"
                if 'F' in res[i][j]:
                  break
                res[i][j] += 'F'
                i += int(m[i][j][1])
            elif now == "B":
                pre = "L"
                if 'L' in res[i][j]:
                    break
                res[i][j] += 'L'
                j -= int(m[i][j][1])
            continue
        if pre == "L":
            if now == "F":
                pre = "L"
                if 'L' in res[i][j]:
                    break
                res[i][j] += 'L'
                j -= int(m[i][j][1])
            elif now == "R":
                pre = "F"
                if 'F' in res[i][j]:
                    break
                res[i][j] += 'F'
                i += int(m[i][j][1])
            elif now == "L":
                pre = "B"
                if 'B' in res[i][j]:
                    break
                res[i][j] += 'B'
                i -= int(m[i][j][1])
            elif now == "B":
                pre = "R"
                if 'R' in res[i][j]:
                    break
                res[i][j] += 'R'
                j += int(m[i][j][1])
            continue            
        if pre == "B":
            if now == "F":
                pre = "B"
                if 'B' in res[i][j]:
                    break
                res[i][j] += 'B'
                i -= int(m[i][j][1])
            elif now == "R":
                pre = "L"
                if 'L' in res[i][j]:
                    break
                res[i][j] += 'L'
                j -= int(m[i][j][1])
            elif now == "L":
                pre = "R"
                if 'R' in res[i][j]:
                    break
                res[i][j] += 'R'
                j += int(m[i][j][1])
            elif now == "B":
                pre = "F"
                if 'F' in res[i][j]:
                    break
                res[i][j] += 'F'
                i += int(m[i][j][1])
            continue
    print(i,j)