# ## 가지치기
# include <iostream>
# include <vector>
# include <queue>
# using namespace std;

# int main(){
#     int t;
#     cin >> t;
#     int dx[] = {-1, 1, 0 ,0};
#     int dy[] = {0, 0, -1, 1};
#     for(int test = 0; test < t; test++){
#         int n;
#         cin >> n;
#         vector<vector<char>> climb(n, vector<char>(n));
#         vector<vector<int>> res(n, vector<int>(n, 0));
#         for (int i = 0; i < n; i++){
#             for (int j = 0; j < n; j++){
#                 char c;
#                 cin >> c;
#                 climb[i][j] = c;
#             }
#         }

#         queue<pair<int, int>> hold;
#         res[n - 1][0] = 1;
#         hold.push({n - 1, 0});

#         while(hold.size() != 0)
#         {
#             int r = hold.front().first;
#             int c = hold.front().second;
#             hold.pop();
#             int h = res[r][c];
            
#             for(int i = 0; i < 4; i++){
#               int nx = r + dx[i];
#               int ny = c + dy[i];
#               if (0 <= nx && nx < n && 0 <= ny && ny < n && climb[nx][ny] == 'H'){
#                 if (res[nx][ny] == 0 or res[nx][ny] > res[r][c]+1){
#                   res[nx][ny] = res[r][c]+1;
#                   hold.push({nx,ny});
#                 }
#               }
#             }

#             if (r > 0 && c - 2 >= 0 && climb[r][c - 1] == '.' && climb[r][c - 2] == 'H' && climb[r - 1][c] == '.' && climb[r - 1][c - 1] == '.' && climb[r - 1][c - 2] == '.' && res[r][c-2] == 0){
#                 res[r][c - 2] = h + 1;
#                 hold.push({r, c - 2});
#             }
#             if (r > 0 && c + 2 <= n - 1 && climb[r][c + 1] == '.' && climb[r][c + 2] == 'H' && climb[r - 1][c] == '.' && climb[r - 1][c + 1] == '.' && climb[r - 1][c + 2] == '.' && res[r][c + 2] == 0){
#               res[r][c + 2] = h + 1;
#               hold.push({r, c + 2});
#             }
#             if (r > 0 && c - 3 >= 0 && climb[r][c - 2] == '.' && climb[r][c - 1] == '.' && climb[r][c - 3] == 'H' && climb[r - 1][c] == '.' && climb[r - 1][c - 1] == '.' && climb[r - 1][c - 2] == '.' && climb[r - 1][c - 3] == '.' && res[r][c - 3]==0){
#               res[r][c - 3] = h + 1;
#               hold.push({r, c - 3});
#             }
#             if (r > 0 && c + 3 >= 0 && climb[r][c + 2] == '.' && climb[r][c + 1] == '.' && climb[r][c + 3] == 'H' && climb[r - 1][c] == '.' && climb[r - 1][c + 1] == '.' && climb[r - 1][c + 2] == '.' && climb[r - 1][c + 3] == '.' && res[r][c + 3] == 0){
#               res[r][c + 3] = h + 1;
#               hold.push({r, c + 3});
#             }
#             if (r >= 2 && climb[r - 1][c] == '.' && climb[r - 2][c] == 'H' && res[r - 2][c] ==0){
#                 res[r - 2][c] = h + 1;
#                 hold.push({r - 2, c});
#             }
#             if (r - 1 >= 0 && c - 1 >= 0 && climb[r][c - 1] == '.' && climb[r - 1][c] == '.' && climb[r - 1][c - 1] == 'H' && res[r - 1][c - 1] ==0){
#                 res[r - 1][c - 1] = h + 1;
#                 hold.push({r - 1, c - 1});
#             }
#             if (r - 1 >= 0 && c + 1 < n && climb[r][c + 1] == '.' && climb[r - 1][c] == '.' && climb[r - 1][c + 1] == 'H' && res[r - 1][c + 1] == 0){
#                 res[r - 1][c + 1] = h + 1;
#                 hold.push({r - 1, c + 1});
#             }
#         }

#         for(int i=0; i<n; i++){
#             for(int j=0; j<n; j++){
#                 if(res[i][j] == 0 && climb[i][j] == 'H'){
#                     res[i][j] = -1;
#                 }
#             }
#         }

#         for(int i=0; i<n; i++){
#             for(int j=0; j<n; j++){
#                 cout << res[i][j] << " ";
#             }
#             cout << endl;
#         }
#     }
#     return 0;
# } 

# 양궁 최대차이

# from itertools import combinations_with_replacement


# def sol(num, l):
#     res = [-1]
#     max_num = -1 

#     for c in combinations_with_replacement(range(11), num):  
#         tmp = [0] * 11  

#         for i in c:  
#             tmp[10 - i] += 1

#         oppo, kor = 0, 0
#         for idx in range(11):
#             if l[idx] == tmp[idx] == 0:
#                 continue
#             elif l[idx] >= tmp[idx]:
#                 oppo += 10 - idx
#             else:  
#                 kor += 10 - idx

#         if kor > oppo: 
#             gap = kor - oppo 
#             if gap > max_num:  
#                 max_num = gap
#                 res = tmp
#     return res
# t = int(input())

# for _ in range(t):
#   arr = list(map(int,input().split()))
#   n = arr[0]
#   del arr[0]
#   korea = sol(n,arr)
#   if korea[0] == -1:
#     print(-1)
#     continue
#   result = 0
#   for i in range(11):
#       if korea[i] > arr[i]:
#         result += (korea[i] - arr[i]) * (10-i)
#       else:
#         continue
#   print(result)

# 과일 숙성

# t = int(input())

# for _ in range(t):
#     n, m = map(int,input().split())
#     box = []
#     apple = []
#     res = 0
#     for _ in range(n):
#         box.append(list(map(int,input().split())))
#     for i in range(n):
#         for j in range(m):
#             if box[i][j] == 1:
#                 apple.append([i,j])
#     while len(apple) != 0:
#         tmp = []
#         for i in apple:
#             r = i[0]
#             c = i[1]
#             if r > 0 and box[r-1][c] == 0:
#                 box[r-1][c] = 1
#                 tmp.append([r-1,c])
#             if c > 0 and box[r][c-1] == 0:
#                 box[r][c-1] = 1
#                 tmp.append([r,c-1])
#             if r < n-1 and box[r+1][c] == 0:
#                 box[r+1][c] = 1
#                 tmp.append([r+1,c])
#             if c < m-1 and box[r][c+1] == 0:
#                 box[r][c+1] = 1
#                 tmp.append([r,c+1])
#         res += 1
#         apple = tmp
#     flag = 0
#     res -= 1
#     for i in range(n):
#         if 0 in box[i]:
#           flag = 1
#           break
#     if flag == 1:
#         print(-1)
#     else:
#         print(res)

# 로봇 청소기

# t = int(input())

# for _ in range(t):
#     n,d = map(int,input().split())
#     r,c = map(int,input().split())
#     arr = []
#     # 0 북, 1 동, 2 남, 3 서
#     dir = [[-1,0],[0,1],[1,0],[0,-1]]
#     for _ in range(n):
#         a = list(map(int,input().split()))
#         arr.append(a)
#     res = 0
#     cnt = 0
#     flag = 0
#     while True:
#         if arr[r][c] == 0:
#             arr[r][c] = -1
#             res += 1
#             cnt = 0
#         while True:
#             if cnt == 4:
#                 d = (d+2)%4
#                 nr = r + dir[d][0]
#                 nc = c + dir[d][1]
#                 if arr[nr][nc] == 1:
#                     flag = 1
#                     break
#                 else:
#                     r = nr
#                     c = nc
#                     d = (d+2)%4
#                     cnt = 0
#                 break
#             nr = r + dir[(d+3)%4][0]
#             nc = c + dir[(d+3)%4][1]

#             if arr[nr][nc] == 0:
#                 r = nr
#                 c = nc
#                 d = (d+3)%4
#                 cnt = 0
#                 break
#             else:
#                 d = (d+3)%4
#                 cnt += 1
#         if flag == 1:
#             break
#     print(res)
    
# 작품 전시

# t = int(input())

# for _ in range(t):
#     n,m = map(int,input().split())
#     arr = list(map(int,input().split()))
#     if m <= n:
#         arr.sort()
#         for i in range(m):
#             print(arr[i],'',end='')
#         print()
#         break 
#     res = [] # 0 작품번호, 1 추천수, 2 순서
#     cnt = 0
#     for _ in range(n):
#         res.append([0,0,-1])
#     for i in range(m):
#         flag = 0
#         for j in range(n):
#             if arr[i] == res[j][0]:
#                 res[j][1] += 1
#                 flag = 1
#         if flag == 1:
#             continue
#         if cnt < n :
#             for q in range(n):
#                 if res[q][0] == 0:
#                     res[q][0] = arr[i]
#                     res[q][1], res[q][2] = 0,i
#                     cnt += 1
#                     break
#             continue
#         order,rec = 99999,99999
#         r_idx = 0
#         o_idx = 0
#         cnt2 = 0
#         for p in range(n):
#             if rec > res[p][1]:
#                 rec = res[p][1]
#                 r_idx = p
#         for u in range(n):
#             if rec == res[u][1]:
#                 cnt2 += 1
#         if cnt2 > 1:
#             for k in range(n):
#                 if rec == res[k][1]:
#                     if order > res[k][2]:
#                         order = res[k][2]
#                         o_idx = k
#             res[o_idx][0] = arr[i]
#             res[o_idx][1], res[o_idx][2] = 0,i
#         else:
#             res[r_idx][0] = arr[i]
#             res[r_idx][1], res[r_idx][2] = 0, i      
#     res.sort()
#     for i in range(n):
#         print(res[i][0],'',end='')
#     print()

# 도어락

# t = int(input())

# for _ in range(t):
#   n, m = map(int,input().split())
#   s1 = input()
#   s2 = input()
#   if s1 in s2 :
#     print(1)
#   else :
#     print(0)
