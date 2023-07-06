import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = list(map(int, input().split()))

res = sum(arr[0:k])
val = res

for i in range(1,n-k+1):
  res = res - arr[i-1] + arr[k-1+i]
  val = max(res,val)
print(val)