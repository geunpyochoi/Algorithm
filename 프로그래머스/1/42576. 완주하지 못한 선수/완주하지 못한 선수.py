def solution(participant, completion):
    dict = {}
    for i in participant:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for j in completion:
        dict[j] -= 1
    for p in participant:
        if dict[p] == 1:
            return p
