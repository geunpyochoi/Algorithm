from itertools import combinations_with_replacement


def sol(num, l):
    res = [-1]
    max_num = -1 

    for c in combinations_with_replacement(range(11), num):  
        tmp = [0] * 11  

        for i in c:  
            tmp[10 - i] += 1

        oppo, kor = 0, 0
        for idx in range(11):
            if l[idx] == tmp[idx] == 0:
                continue
            elif l[idx] >= tmp[idx]:
                oppo += 10 - idx
            else:  
                kor += 10 - idx

        if kor > oppo: 
            gap = kor - oppo 
            if gap > max_num:  
                max_num = gap
                res = tmp
    return res
  
t = int(input())

for _ in range(t):
  arr = list(map(int,input().split()))
  n = arr[0]
  del arr[0]
  korea = sol(n,arr)
  if korea[0] == -1:
    print(-1)
    continue
  result = 0
  for i in range(11):
      if korea[i] > arr[i]:
        result += (korea[i] - arr[i]) * (10-i)
      else:
        continue
  print(result)