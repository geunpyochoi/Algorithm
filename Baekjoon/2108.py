from collections import Counter

n = int(input())
arr = []
for i in range(0,n):
  num = int(input())
  arr.append(num)
  
arr.sort()
san = round(sum(arr)/n)
print(san)

mid = arr[(int(len(arr)/2))]
print(mid)

if len(arr) > 1 : 
    if cnt_li[0][1] == cnt_li[1][1]:
      bin = cnt_li[1][0]
    else : 
      bin = cnt_li[0][0]
else : 
    bin = cnt_li[0][0]
print(bin)

val = arr[-1] - arr[0]
print(val)