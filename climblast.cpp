#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main(){
    int t;
    cin >> t;
    int dx[] = {-1, 1, 0 ,0};
    int dy[] = {0, 0, -1, 1};
    for(int test = 0; test < t; test++){
        int n;
        cin >> n;
        vector<vector<char>> climb(n, vector<char>(n));
        vector<vector<int>> res(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                char c;
                cin >> c;
                climb[i][j] = c;
            }
        }

        queue<pair<int, int>> hold;
        res[n - 1][0] = 1;
        hold.push({n - 1, 0});

        while(hold.size() != 0)
        {
            int r = hold.front().first;
            int c = hold.front().second;
            hold.pop();
            int h = res[r][c];
            
            for(int i = 0; i < 4; i++){
              int nx = r + dx[i];
              int ny = c + dy[i];
              if (0 <= nx && nx < n && 0 <= ny && ny < n && climb[nx][ny] == 'H'){
                if (res[nx][ny] == 0 or res[nx][ny] > res[r][c]+1){
                  res[nx][ny] = res[r][c]+1;
                  hold.push({nx,ny});
                }
              }
            }

            if (r > 0 && c - 2 >= 0 && climb[r][c - 1] == '.' && climb[r][c - 2] == 'H' && climb[r - 1][c] == '.' && climb[r - 1][c - 1] == '.' && climb[r - 1][c - 2] == '.' && res[r][c-2] == 0){
                res[r][c - 2] = h + 1;
                hold.push({r, c - 2});
            }
            if (r > 0 && c + 2 <= n - 1 && climb[r][c + 1] == '.' && climb[r][c + 2] == 'H' && climb[r - 1][c] == '.' && climb[r - 1][c + 1] == '.' && climb[r - 1][c + 2] == '.' && res[r][c + 2] == 0){
              res[r][c + 2] = h + 1;
              hold.push({r, c + 2});
            }
            if (r > 0 && c - 3 >= 0 && climb[r][c - 2] == '.' && climb[r][c - 1] == '.' && climb[r][c - 3] == 'H' && climb[r - 1][c] == '.' && climb[r - 1][c - 1] == '.' && climb[r - 1][c - 2] == '.' && climb[r - 1][c - 3] == '.' && res[r][c - 3]==0){
              res[r][c - 3] = h + 1;
              hold.push({r, c - 3});
            }
            if (r > 0 && c + 3 >= 0 && climb[r][c + 2] == '.' && climb[r][c + 1] == '.' && climb[r][c + 3] == 'H' && climb[r - 1][c] == '.' && climb[r - 1][c + 1] == '.' && climb[r - 1][c + 2] == '.' && climb[r - 1][c + 3] == '.' && res[r][c + 3] == 0){
              res[r][c + 3] = h + 1;
              hold.push({r, c + 3});
            }
            if (r >= 2 && climb[r - 1][c] == '.' && climb[r - 2][c] == 'H' && res[r - 2][c] ==0){
                res[r - 2][c] = h + 1;
                hold.push({r - 2, c});
            }
            if (r - 1 >= 0 && c - 1 >= 0 && climb[r][c - 1] == '.' && climb[r - 1][c] == '.' && climb[r - 1][c - 1] == 'H' && res[r - 1][c - 1] ==0){
                res[r - 1][c - 1] = h + 1;
                hold.push({r - 1, c - 1});
            }
            if (r - 1 >= 0 && c + 1 < n && climb[r][c + 1] == '.' && climb[r - 1][c] == '.' && climb[r - 1][c + 1] == 'H' && res[r - 1][c + 1] == 0){
                res[r - 1][c + 1] = h + 1;
                hold.push({r - 1, c + 1});
            }
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(res[i][j] == 0 && climb[i][j] == 'H'){
                    res[i][j] = -1;
                }
            }
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                cout << res[i][j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}