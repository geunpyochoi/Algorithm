import math
def prime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if(num % i == 0) :
            return False
    return True

def solution(n):
    answer = 1
    for i in range(3,n+1):
        if (prime(i)):
            answer += 1
    return answer