
n = int(input())
dic = {}
for i in range(n):
  b = input()
  if b in dic:
    dic[b] += 1
  else : dic[b] = 1
  
max_value = max(dic.values())
max_keys = [key for key, value in dic.items() if value == max_value]
max_keys.sort()

print(max_keys[0])