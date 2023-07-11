max_num = -1
res = []
    
def sol(num, l):
  def cal(oppo, kor):
        oppoScore, korScore = 0, 0
        for i in range(11):
            if oppo[i] == 0 and kor[i] == 0:
              continue
            elif oppo[i] > kor[i]:
                oppoScore += 10 - i
            else:
                korScore += 10 - i
        return oppoScore, korScore
    
  def dfs(kor, idx):
      global max_num, res
      
      if idx == 11:
          o, k = 0, 0
          if sum(kor) == num:
              o, k = cal(l, kor)
          elif sum(kor) < num:
              kor[-1] += (num - sum(kor))
              o, k = cal(l, kor)
          else:
              return
          if o < k:
              if max_num < (k-o):
                  max_num = (k-o)
                  res = [kor[:]]
              elif max_num == (k-o):
                  res.append(kor[:])
          return
      
      kor.append(l[idx]+1)
      dfs(kor, idx+1)
      kor.pop()
      
      kor.append(0)
      dfs(kor, idx+1)
      kor.pop()
    
  dfs([], 0)
  if not res: 
    return [-1]

  res.sort(key=lambda x: x[::-1], reverse=True)    
  return res[0]


t = int(input())

for _ in range(t):
  arr = list(map(int,input().split()))
  n = arr[0]
  del arr[0]
  korea= sol(n,arr)
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