function solution(n) {
    var answer = 0;
    for(i = 2; i < n; i++){
        if (n % i == 1){
            answer = i;
            break;
        }
    }
    return answer;
}