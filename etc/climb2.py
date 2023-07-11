from collections import deque

t = int(input())
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]
for i in range(t):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(str, input().split())))
    
    visited = [[0] * n for _ in range(n)]
    visited[n-1][0] = 1
    check_list = deque()
    check_list.append((n-1, 0))
    while check_list:
        now = check_list.popleft()
        x = now[0]
        y = now[1]
        for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == "H":
                    if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y]+1:
                        visited[nx][ny] = visited[x][y]+1
                        check_list.append((nx,ny))
        if x-2 >=0 and graph[x-1][y] == '.' and graph[x-2][y] == "H":
            if visited[x-2][y] == 0 or visited[x-2][y] > visited[x][y]+1:
                visited[x-2][y] = visited[x][y] +1
                check_list.append((x-2,y))
        if (x-1 >=0 and y-1 >=0) and graph[x][y-1] == '.' and graph[x-1][y] == '.' and graph[x-1][y-1] == 'H':
            if visited[x-1][y-1] == 0 or visited[x-1][y-1] > visited[x][y]+1:
                visited[x-1][y-1] = visited[x][y] +1
                check_list.append((x-1,y-1))
        if (x-1 >=0 and y+1 < n) and graph[x][y+1] == '.' and graph[x-1][y] == '.' and graph[x-1][y+1] == 'H':
            if visited[x-1][y+1] == 0 or visited[x-1][y+1] > visited[x][y]+1:
                visited[x-1][y+1] = visited[x][y] +1
                check_list.append((x-1,y+1))
        ##########
        if (y+2 < n and x-1 >= 0 ) and graph[x][y] == "H" and graph[x][y+2] == "H" and graph[x][y+1] == ".":
            if graph[x-1][y] == '.' and graph[x-1][y+1] =='.' and graph[x-1][y+2] =='.':
                if visited[x][y+2] == 0 or visited[x][y+2] > visited[x][y]+1:
                    visited[x][y+2] = visited[x][y] +1
                    check_list.append((x,y+2))
        if (y-2 >=0 and x-1 >= 0 ) and graph[x][y] == "H" and graph[x][y-2] == "H" and graph[x][y-1] == ".":
            if graph[x-1][y] == '.'and graph[x-1][y-1] =='.' and graph[x-1][y-2] =='.':
                if visited[x][y-2] == 0 or visited[x][y-2] > visited[x][y]+1:
                    visited[x][y-2] = visited[x][y] +1
                    check_list.append((x,y-2))
        if (y+3 < n and x-1 >= 0 ) and graph[x][y] == "H" and graph[x][y+3] == "H" and graph[x][y+1] == "." and graph[x][y+2]==".":
            if graph[x-1][y] =='.' and graph[x-1][y+1] =='.' and graph[x-1][y+2] =='.' and graph[x-1][y+3]== '.':
                if visited[x][y+3] == 0 or visited[x][y+3] > visited[x][y]+1:
                    visited[x][y+3] = visited[x][y] +1
                    check_list.append((x,y+3))
        if (y-3>=0 and x-1 >= 0 ) and graph[x][y] == "H" and graph[x][y-3] == "H" and graph[x][y-1] == "." and graph[x][y-2]==".":
            if graph[x-1][y] =='.' and graph[x-1][y-1] =='.' and graph[x-1][y-2] =='.' and graph[x-1][y-3]== '.':
                if visited[x][y-3] == 0 or visited[x][y-3] > visited[x][y]+1:
                    visited[x][y-3] = visited[x][y] +1
                    check_list.append((x,y-3))
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "H":
                if visited[i][j] == 0 :
                    visited[i][j] = -1
    for i in range(0, n):
        for j in range(0,n):
            print(visited[i][j], end = ' ')
        print("")