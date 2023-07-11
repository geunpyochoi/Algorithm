#include <iostream>
using namespace std;

int g[1002];

int main(){
  int t;
  cin >> t;
  for(int test = 0; test < t; test++){
    int n;
    cin >> n;
    g[1] = 1;
    int idx = 1;
    int s = 1;
    while (s < n)
    {
      idx++;
      g[idx] = 1 + g[idx - g[g[idx - 1]]];
      s += g[idx];
    }
    cout << idx << endl;
  }
}