def solution(arr1, arr2):
    answer = []
    n = 0
    for i in range(len(arr1)): # 0 1     
        answer.append([])
        for j in range(len(arr2[0])):# 0 1 2 3  0 1
            for k in range(len(arr1[0])): #0 1   0 1
                n += arr1[i][k] * arr2[k][j]                
            answer[i].append(n)
            n = 0
    return answer