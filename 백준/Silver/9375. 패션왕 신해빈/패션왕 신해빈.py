import sys
input = sys.stdin.readline

t = int(input()) 
for i in range(t):
    n = int(input()) 
    clothes = {}
    for j in range(n):
        c_n, c_t = input().split() 

        if c_t not in clothes.keys():
            clothes[c_t] = 1
        else:
            clothes[c_t] += 1
    
    ans = 1
    for i in clothes: 
        ans *= (clothes[i]+1) 
    print(ans-1) 