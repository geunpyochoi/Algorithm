import sys
t = int(input())

for _ in range(0,t):
    n = int(input())
    l = input().split()
    num = []
    stack = []
    prior = {'*':3,'+':2,'-':2,'(':1}
    for i in range(0,len(l)):
        if l[i].isdigit():
          num.append(l[i])
        elif l[i] == '(':
            stack.append(l[i])
        elif l[i] == ')':
            while stack[-1] != '(':
                num.append(stack.pop())
            stack.pop() 
        else: 
            while stack and prior[l[i]] <= prior[stack[-1]]:
                num.append(stack.pop()) 
            stack.append(l[i])
    while len(stack) != 0:
        num.append(stack.pop())
    n1 = 0
    n2 = 0
    b = len(num)
    for j in range(0,b):
        if num[j].isdigit():
            stack.append(int(num[j]))
        elif num[j] == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1+n2)
        elif num[j] == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
        elif num[j] == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1*n2)
    print(stack[0])
            
