function solution(n) {
    var answer = 0;
    for (i = 4; i <= n; i++){
        for(j = 2; j < i; j++){
            if (i % j == 0){
                answer += 1;
                break;
            }
        }
    }
    return answer;
}