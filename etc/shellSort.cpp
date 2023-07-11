#include <iostream>
using namespace std;

#define MAX_SIZE 1000
void ShellSort(int a[], int n);

int main(){
    int t;
    cin >> t;
    for(int test = 0; test < t; test++){
        int num;
        int a[MAX_SIZE];
        cin >> num;
        for(int j = 0; j < num; j++)
        cin >> a[j];
        ShellSort(a,num);
    }
    return 0;
}

void swap(int* a, int* b)
{
 int tmp = *a;
 *a = *b;
 *b = tmp;
}

/* comb sort 함수 */
void ShellSort(int a[], int n)
{
    int countCmpOps = 0; // 비교 연산자 실행 횟수
    int countSwaps = 0; // swap 함수 실행 횟수
    int i, j, k, temp;
	  for(i = n/2; i > 0; i = i/2)
	  {
		  for(j = i; j < n; j++)
		  {
        countCmpOps++;
			  for(k = j-i; k >= 0; k = k-i)
			  {
					if(a[k+i] >= a[k])
				  break;
				  else
				  { 
            countSwaps++;
					  temp = a[k];
					  a[k] = a[k+i];
					  a[k+i] = temp;
				  }
			  }
		  }
	  }
    cout << countCmpOps<< " " << countSwaps << " " << endl;
}