t = int(input())

for _ in range(t):
    n = int(input())
    num_list = list(map(int,input().split()))
    num = []
    for i in range(n):
        num.append([num_list[i],num_list[i+1]])
    s = input()
    stack = []
    m = ""
    val = 0
    for i in range(0,len(s)):
        res = 0
        chain = ["",""]
        if s[i] == ')':
            while stack[-1] != '(':
                m += stack.pop()
            stack.pop()
            tmp = -1
            c1,c2 = "",""
            k = -1
            for j in range(len(m)-1,-1,-1):
              if m[j].isdigit():
                chain[k] += m[j]
              else:
                k += 1
            c1 = int(chain[0]) - 1
            c2 = int(chain[1]) - 1
            if c1 > c2 :
                tmp = c1
                c1 = c2
                c2 = tmp
            res += num[c1][0] * num[c1][1] * num[c2][0] * num[c2][1]
            res /= num[c2][0]
            if c2-c1 > 1 :
              for j in range(c1+1,c2):
                num[j][0] = num[c1][0]
                num[j][1] = num[c2][1]
            val += int(res)
            num[c1][1] = num[c2][1]
            num[c2][0] = num[c1][0]
            m = ""
            stack.append("m")
            if c2 >= 10 :
              stack.append(str(int(c2/10)))
              stack.append(str(c2%10))
            else:
              stack.append(str(c2))
        else :
            stack.append(s[i])
    print(val)