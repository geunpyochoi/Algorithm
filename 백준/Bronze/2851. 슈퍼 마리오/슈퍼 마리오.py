l = []
for i in range(10):
    l.append(int(input()))
    
answer = 0
for j in l:
    if abs(100-answer) < abs(100-answer-j):
        break
    else:
        answer += j
print(answer)