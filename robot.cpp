#include <iostream>
#include <vector>

using namespace std;

int box[501][501];

int main(){
  int t;
  cin >> t;
  for(int test = 0; test < t; test++){
    int n,m;
    cin >> n >> m;
    vector<vector<int>> apple;
    int res = 0;
    for(int i = 0; i < n; i++){
      for(int j = 0; j < m; j++){
        int a;
        cin >> a;
        box[i][j] = a;
      }
    }
    for(int i = 0; i < n; i++){
      for(int j = 0; j < m; j++){
        if (box[i][j] == 1){
          vector<int> v;
          v.push_back(i);
          v.push_back(j);
          apple.push_back(v);
        }
      }
    }
    while (apple.size() != 0){
      vector<vector<int>> tmp;
      for (int i = 0; i < apple.size(); i++){
        int r = apple[i][0];
        int c = apple[i][1];
        vector<int> v2;
        if (r > 0 && box[r-1][c] == 0){
          box[r-1][c] = 1;
          v2.push_back(r-1);
          v2.push_back(c);
          tmp.push_back(v2);
        }
        vector<int> v3;
        if (c > 0 && box[r][c-1] == 0){
          box[r][c-1] = 1;
          v3.push_back(r);
          v3.push_back(c-1);
          tmp.push_back(v3);
        }
        vector<int> v4;
        if (r < n-1 && box[r+1][c] == 0){
          box[r+1][c] = 1;
          v4.push_back(r+1);
          v4.push_back(c);
          tmp.push_back(v4);
        }
        vector<int> v5;
        if (c < m-1 && box[r][c+1] == 0){
          box[r][c+1] = 1;
          v5.push_back(r);
          v5.push_back(c+1);
          tmp.push_back(v5);
        }
      }
      res++;
      apple = tmp;
    }
    int flag = 0;
    res--;
    for(int i = 0; i < n; i++){
      for(int j = 0; j < m; j++){
        if (box[i][j] == 0){
          flag = 1;
          break;
        }
      }
      if (flag == 1){
        break;
      }
    }
    if (flag == 1){
      cout << -1 << endl;
    }
    else{
      cout << res << endl;
    }

  }
  return 0;
}