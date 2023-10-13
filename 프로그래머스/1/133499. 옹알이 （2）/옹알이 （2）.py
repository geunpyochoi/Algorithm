def solution(babbling):
    answer = 0
    w = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in w:
            if j*2 not in i :
                i = i.replace(j,' ')
        if(i.strip() == ''):
            answer += 1
    return answer