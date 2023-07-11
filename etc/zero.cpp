#include <iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int test = 0; test < t; test++){
        int n;
        cin >> n;
        int num;
        int five = 0;
        int two = 0;
        int val = 1;
        for(int i = 0; i < n; i++){
            cin >> num;
            while (num % 2 == 0 || num % 5 == 0){
              if (num % 2 == 0){
                two++;
                num /= 2;
              }
              else{
                five++;
                num /= 5;
              }
            }
            val *= num % 10;
            val %= 10;
        }

        int cnt,sub = 0;
        if (five < two){
            cnt = five;
            sub = two - five;
            for(int i = 0; i < sub; i++){
              val *= 2;
              val %= 10;
            }
        }
        else{
            cnt = two;
            sub = five - two;
            for(int i = 0; i < sub; i++){
              val *= 5;
              val %= 10;
            }
        }
        cout << val << " " << cnt << endl;
        }
       return 0;
    }
    