#include <iostream>
using namespace std;

#define MAX_SIZE 1000
void insertionSort(int a[], int n);

int main(){
    int t;
    cin >> t;
    for(int test = 0; test < t; test++){
        int num;
        int a[MAX_SIZE];
        cin >> num;
        for(int j = 0; j < num; j++)
        cin >> a[j];
        insertionSort(a,num);
    }
    return 0;
}

void insertionSort(int a[], int n)
{
  int countCmpOps = 0; // 비교 연산자 실행 횟수
  int countSwaps = 0; // swap 함수 실행 횟수
  // insertion sort 알고리즘 구현
  int temp;
  for (int i = 0; i < n - 1; i++) {
	for (int j = i + 1; j > 0; j--) {
        countCmpOps++;
		if (a[j] < a[j-1]) {
            countSwaps++;
			temp = a[j-1];
			a[j-1] = a[j];
			a[j] = temp;
		}
		else
			break;
		}

  }
    cout << countCmpOps<< " " << countSwaps << " " << endl;
}